loc_ls_left = []
loc_ls_right = []

with open("input.txt") as input_1:
    for line in input_1:
        num1, num2 = line.split()
        loc_ls_left.append(int(num1))
        loc_ls_right.append(int(num2))

loc_ls_left.sort()
loc_ls_right.sort()

total_distance = 0
for num1, num2 in zip(loc_ls_left, loc_ls_right):
    total_distance+= abs(num1 - num2)

# 2970687
print(f"Total distance: {total_distance}")

loc_ls_right_counts = {}
for num in loc_ls_right:
    loc_ls_right_counts[num] = loc_ls_right_counts.setdefault(num, 0) + 1


similarity_score = 0
for num in loc_ls_left:
    similarity_score += loc_ls_right_counts.get(num, 0) * num

# 23963899
print(f"Similarity score: {similarity_score}")
