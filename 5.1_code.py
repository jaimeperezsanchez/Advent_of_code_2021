with open('./5_input.txt', 'r') as f:
    data = f.readlines()

danger_points = []
for line in data:
    start = line.split("->")[0].split(",")
    end = line.split("->")[1].split(",")
    x1 = int(start[0])
    y1 = int(start[1])
    x2 = int(end[0])
    y2 = int(end[1])
    # Horizontal lines
    if x1 == x2:
        if y1 < y2:
            for i in range(y1, y2 + 1):
                danger_points.append((x1, i))
        elif y1 > y2:
            for i in range(y2, y1 + 1):
                danger_points.append((x1, i))
        else:  # Single poing (x1 == x2 and y1 == y2)
            danger_points.append((x1, y1))
    # Vertical lines
    elif y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                danger_points.append((i, y1))
        elif x1 > x2:
            for i in range(x2, x1 + 1):
                danger_points.append((i, y1))
# Find duplicate points
extreme_danger_points = {
    n for n in danger_points if danger_points.count(n) > 1
}
# Print number of extreme danger points (with 2 or more occurrences)
print(len(extreme_danger_points))