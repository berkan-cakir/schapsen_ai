FILE_NAME = "rdeep_vs_ml_inverserdeep_kbbot_bully_rand.txt"
SEPARATOR = ":"


def get_points(line):
    line_split = line.split(SEPARATOR)
    points = line_split[1].rstrip()
    point_a = points.split(",")[0].rstrip()[2:]
    point_b = points.split(",")[1].rstrip()[:-1]
    return int(point_a), int(point_b)


lines = open(FILE_NAME).readlines()

win_a = 0
win_b = 0
points_a = 0
points_b = 0
old_points_a = 0
old_points_b = 0

for count, line in enumerate(lines):
    if count >= 1 and count <= 125:
        points = get_points(line)

        points_a += points[0] - old_points_a
        points_b += points[1] - old_points_b

        old_points_a = points[0]
        old_points_b = points[1]

    if points_a >= 7:
        win_a += 1
        points_a = 0
        points_b = 0
    elif points_b >= 7:
        win_b += 1
        points_a = 0
        points_b = 0

print("bot_a: {}, bot_b: {}".format(win_a, win_b))