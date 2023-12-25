#!/usr/bin/env python3

import numpy
from skspatial.objects import Line


class Hailstone:
    def __init__(self, start, velocity):
        self.start = start
        self.velocity = velocity
        self.line = Line(start, velocity)

    def __repr__(self):
        return repr((self.start, " @ ", self.velocity, self.line))

    def point_is_future(self, point):
        """steps to reach point must be positive on both x & y
        if point is in future for"""
        x = (point[0] - self.start[0]) / self.velocity[0]
        y = (point[1] - self.start[1]) / self.velocity[1]
        if x < 0 or y < 0:
            return False
        else:
            return True


def parser(record):
    p, v = record.strip().split("@")
    p = [int(a.strip()) for a in p.split(",")[:2]]
    v = [int(a.strip()) for a in v.split(",")[:2]]
    return p, v


def check_same_line(hs1, hs2, min):
    t = (min - hs1.start[0]) / hs1.velocity[0]
    y1 = hs1.start[1] + hs1.velocity[1] * t
    y2 = hs2.start[1] + hs2.velocity[1] * t
    if y1 == y2:
        return True, numpy.array([min, y1])
    else:
        return False, numpy.array([])


def main_part_1(data, min, max):
    """Parse data and set up the list of hailstones
    For each pair of hailstones:
    - Handle parallel lines
    - Find intersection if it exists
    - Test intersection in test area
    - Test intersection in future for stone
    """
    hailstones = []
    for record in data.strip().split("\n"):
        p, v = parser(record)
        hailstones.append(Hailstone(start=p, velocity=v))

    intersections = 0
    for i in range(0, len(hailstones) - 1):
        for j in range(i + 1, len(hailstones)):
            hs1, hs2 = hailstones[i], hailstones[j]
            # find intersection
            try:
                intersection = hs1.line.intersect_line(hs2.line)
            except:
                result, i = check_same_line(hs1, hs2, min)
                if result:
                    intersection = i
                else:
                    intersection = numpy.array([])
            if intersection.any():
                # is intersection in test area?
                if not (
                    min <= intersection[0]
                    and intersection[0] <= max
                    and min <= intersection[1]
                    and intersection[1] <= max
                ):
                    break
                # is intersection future to both hailstones?
                if hs1.point_is_future(point=intersection) and hs2.point_is_future(
                    point=intersection
                ):
                    # print(hs1, hs2, intersection)
                    intersections += 1

    return intersections
