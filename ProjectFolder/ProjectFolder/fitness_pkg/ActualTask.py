"""Fitness Activity Analyzer - function definitions (uses sample data only)."""

VALID_DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")


def add_activity(log, day, activity, minutes):
    """Add one activity to the weekly log (a list of dictionaries).

    Validates the day, activity name and duration, then returns the log.
    """
    if day not in VALID_DAYS:
        raise ValueError(f"Invalid day '{day}'. Use one of {VALID_DAYS}")
    if not isinstance(activity, str) or activity.strip() == "":
        raise ValueError("Activity name cannot be empty")
    if not isinstance(minutes, (int, float)) or minutes <= 0:
        raise ValueError("Minutes must be a number greater than zero")
    log.append({"day": day, "activity": activity.strip().title(), "minutes": minutes})
    return log


def weekly_total(log):
    """Return total minutes for the week and a per-day breakdown (dictionary)."""
    per_day = {}
    total = 0
    for entry in log:
        per_day[entry["day"]] = per_day.get(entry["day"], 0) + entry["minutes"]
        total += entry["minutes"]
    return total, per_day


def average_duration(log):
    """Return the average duration (minutes) of one activity session."""
    if len(log) == 0:
        raise ValueError("No activities recorded - cannot calculate average")
    total, _ = weekly_total(log)
    return total / len(log)


def goal_status(log, goal_minutes):
    """Compare weekly total with a goal; return (percentage, message)."""
    if goal_minutes <= 0:
        raise ValueError("Goal must be greater than zero")
    total, _ = weekly_total(log)
    percent = (total / goal_minutes) * 100
    if percent >= 100:
        message = "Goal achieved!"
    elif percent >= 50:
        message = f"Keep going - {goal_minutes - total} minutes left"
    else:
        message = f"Behind target - {goal_minutes - total} minutes left"
    return percent, message
