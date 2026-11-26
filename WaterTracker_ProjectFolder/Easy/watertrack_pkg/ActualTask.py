"""Daily Water Intake Tracker - function definitions (sample data only)."""


def record_intake(intake_list, ml):
    """Add one drink (in ml) to today's list after checking the value."""
    if not isinstance(ml, (int, float)) or ml <= 0:
        raise ValueError("Water amount must be a number greater than zero")
    intake_list.append(ml)
    return intake_list


def target_status(total_ml, target_ml):
    """Compare total water with the daily target and return a message."""
    if target_ml <= 0:
        raise ValueError("Target must be greater than zero")
    if total_ml >= target_ml:
        return "Target achieved!"
    remaining = target_ml - total_ml
    return f"{remaining} ml remaining"


def daily_summary(intake_list, target_ml):
    """Return number of drinks, total ml, percentage and status."""
    total = sum(intake_list)
    percent = (total / target_ml) * 100 if target_ml > 0 else 0
    status = target_status(total, target_ml)
    return len(intake_list), total, percent, status
