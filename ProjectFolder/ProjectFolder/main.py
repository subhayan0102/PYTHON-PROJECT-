from fitness_pkg import add_activity, weekly_total, average_duration, goal_status

GOAL = 150  # WHO-style weekly goal in minutes (sample value)

print("=== Test 1: Normal week (goal achieved) ===")
log = []
add_activity(log, "Mon", "running", 40)
add_activity(log, "Wed", "cycling", 50)
add_activity(log, "Fri", "yoga", 30)
add_activity(log, "Sat", "football", 45)
total, per_day = weekly_total(log)
print("Total minutes :", total)
print("Per day       :", per_day)
print(f"Average/session: {average_duration(log):.2f} min")
pct, msg = goal_status(log, GOAL)
print(f"Goal progress : {pct:.1f}% -> {msg}")

print("\n=== Test 2: Partial week (goal not met) ===")
log2 = []
add_activity(log2, "Tue", "walking", 30)
add_activity(log2, "Thu", "swimming", 40)
pct, msg = goal_status(log2, GOAL)
print(f"Total: {weekly_total(log2)[0]} min | {pct:.1f}% -> {msg}")

print("\n=== Test 3: Edge case - empty log ===")
try:
    average_duration([])
except ValueError as e:
    print("Error caught:", e)

print("\n=== Test 4: Invalid inputs ===")
for args in [("Funday", "yoga", 30), ("Mon", "  ", 30), ("Mon", "yoga", -5)]:
    try:
        add_activity([], *args)
    except ValueError as e:
        print("Error caught:", e)

print("\n=== Test 5: Boundary - exactly at goal ===")
log3 = []
add_activity(log3, "Sun", "hiking", 150)
print(goal_status(log3, GOAL))
