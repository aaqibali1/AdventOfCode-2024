import re
import z3

with open("input") as f:
    clusters = [
        list(map(int, re.findall("\\d+", cluster))) for cluster in f.read().strip().split("\n\n")
    ]


def compute_cost(p1x, p1y, p2x, p2y, target_x, target_y, offset=0):
    target_x += offset
    target_y += offset
    x_factor = z3.Int("x_factor")
    y_factor = z3.Int("y_factor")
    solver = z3.Solver()
    solver.add(x_factor * p1x + y_factor * p2x == target_x)
    solver.add(x_factor * p1y + y_factor * p2y == target_y)
    solver.add(x_factor >= 0)
    solver.add(y_factor >= 0)
    if solver.check() == z3.sat:
        model = solver.model()
        return 3 * model[x_factor].as_long() + model[y_factor].as_long()
    return 0


# Part 1
print(sum(compute_cost(*cluster) for cluster in clusters))

# Part 2
print(sum(compute_cost(*cluster, 10000000000000) for cluster in clusters))
