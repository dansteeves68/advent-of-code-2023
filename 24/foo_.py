#!/usr/bin/env python3


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return repr((self.x, self.y, self.z))


class Hailstone:
    def __init__(self, record):
        p, v = record.strip().split("@")
        self.px, self.py, self.pz = [int(a.strip()) for a in p.split(",")]
        self.vx, self.vy, self.vz = [int(a.strip()) for a in v.split(",")]

    def __repr__(self):
        return repr((self.px, self.py, self.pz, " @ ", self.vx, self.vy, self.vz))

    def projection(self, time):
        pp = Point(
            x=self.px + self.vx * time,
            y=self.py + self.vy * time,
            z=self.pz + self.vz * time,
        )
        return pp

    def time_to_x(self, x):
        return (x - self.px) / self.vx

    def time_to_y(self, y):
        return (y - self.py) / self.vy


def main_part_1(data, max_x, max_y):
    hailstones = []
    intersections = 0
    for record in data.strip().split("\n"):
        hailstones.append(Hailstone(record=record))

    hs_times = []
    for h in hailstones:
        t = []
        for x in [0, max_x]:
            t.append(h.time_to_x(x=x))
        for y in [0, max_y]:
            t.append(h.time_to_y(y=y))
        hs_times.append((min(t), max(t)))

    for i in range(0, len(hailstones_p) - 1):
        for j in range(i, len(hailstones_p)):
            t = hs_times[i] + hs_times[j]
            t_min, t_max = min(t), max(t)
            a, b = hailstones_p[i]
            c, d = hailstones_p[j]
            if intersect(a, b, c, d):
                print("Intersection ", hailstones[i], hailstones[j])
                intersections += 1


def ccw(a, b, c):
    return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)


def intersect(a, b, c, d):
    return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)
