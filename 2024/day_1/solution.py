import collections as _collections

loc_ls_left = []
loc_ls_right = []

with open("input.txt") as input_1:
    for line in input_1:
        num1, num2 = map(int, line.split())
        loc_ls_left.append(num1)
        loc_ls_right.append(num2)

loc_ls_left.sort()
loc_ls_right.sort()

total_distance = sum(
    abs(num1 - num2) for num1, num2
    in zip(loc_ls_left, loc_ls_right)
)
# 2970687
print(f"Total distance: {total_distance}")

right_id_counts = _collections.Counter(loc_ls_right)
similarity_score = sum(right_id_counts.get(num, 0) * num for num in loc_ls_left)

# 23963899
print(f"Similarity score: {similarity_score}")
