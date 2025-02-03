with open("input.txt") as input_f:
    reports = [list(map(int, line.strip().split())) for line in input_f]

safe_count = 0
for s_report in reports:
    unsafe = False
    level_differences = []

    for index, _ in enumerate(s_report[1:], start=1):
        l_difference = s_report[index] - s_report[index - 1]
        level_differences.append(l_difference)

        if abs(l_difference) < 1 or abs(l_difference) > 3:
            unsafe = True
            continue

    if not unsafe:
        negatives_count = len([x for x in level_differences if x < 0])
        if negatives_count == 0:
            # All differences are positive. Levels are gradually increasing.
            safe_count += 1
            continue

        if negatives_count == len(level_differences):
            # All differences are negative. Levels are gradually decreasing.
            safe_count += 1
            continue

# 534
print(f"Safe count: {safe_count}")