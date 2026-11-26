from watertrack_pkg import record_intake, target_status, daily_summary

TARGET = 2000 

print("=== Test 1: Normal day (target achieved) ===")
day1 = []
for amount in [500, 300, 700, 250, 400]:
    record_intake(day1, amount)
drinks, total, percent, status = daily_summary(day1, TARGET)
print("Drinks :", drinks)
print("Total  :", total, "ml")
print(f"Progress: {percent:.1f}%")
print("Status :", status)

print("\n=== Test 2: Partial day (target not met) ===")
day2 = []
record_intake(day2, 600)
record_intake(day2, 400)
print(daily_summary(day2, TARGET))

print("\n=== Test 3: Edge case - no water recorded ===")
print(daily_summary([], TARGET))

print("\n=== Test 4: Invalid inputs ===")
try:
    record_intake([], -250)
except ValueError as e:
    print("Error caught:", e)
try:
    target_status(500, 0)
except ValueError as e:
    print("Error caught:", e)

print("\n=== Test 5: Boundary - exactly at target ===")
print(target_status(2000, TARGET))
