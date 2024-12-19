import time
def is_safe_report(report):
    """Check if a report is safe without removing any levels."""
    asc = None
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        # Check if difference is out of bounds
        if abs(diff) < 1 or abs(diff) > 3:
            return False

        # Determine direction on the first step
        if asc is None:
            asc = diff > 0

        # Ensure direction is consistent
        if (diff > 0 and not asc) or (diff < 0 and asc):
            return False

    return True


def is_safe_with_dampener(report):
    """Check if a report is safe with the Problem Dampener, skipping one level."""
    asc = None
    skip_used = False
    last_valid_index = 0  # Tracks the last valid level's index

    for i in range(1, len(report)):
        if skip_used:
            diff = report[i] - report[last_valid_index]  # Compare to the last valid level
        else:
            diff = report[i] - report[i - 1]  # Normal comparison

        # Check if difference is out of bounds
        if abs(diff) < 1 or abs(diff) > 3:
            if skip_used:
                return False  # Can't skip twice
            skip_used = True  # Use dampener by skipping this level
            continue  # Skip this level and move to the next

        # Determine direction on the first valid step
        if asc is None:
            asc = diff > 0

        # Ensure direction is consistent
        if (diff > 0 and not asc) or (diff < 0 and asc):
            if skip_used:
                return False  # Can't skip twice
            skip_used = True  # Use dampener by skipping this level
            continue  # Skip this level and move to the next

        # Update the last valid index
        last_valid_index = i  # Update to the current valid level

    return True


safe_reports = 0

with open('two.csv') as input:
    start = time.time()
    for line in input:
        report = list(map(int, line.split()))

        # First, check if the report is safe as is
        if is_safe_report(report):
            safe_reports += 1
            continue

        # If not, check if it's safe with the dampener
        if is_safe_with_dampener(report):
            safe_reports += 1
    end = time.time()

print(f'time taken: {(end - start)* 10**3}ms')
print(safe_reports)