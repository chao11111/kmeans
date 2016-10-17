# -*- coding: utf-8 -*-

import math
import random
MAX = 200000


def distance(p, q):
    return ((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)


def which_cluster(p, reps):
    n = len(reps)
    dist = MAX
    which = 0
    for i in range(n):
        cand = distance(p, reps[i])
        if cand < dist:
            dist = cand
            which = i
    return which


def avarage_color(points):
    n = len(points)
    if n == 0:
        return (0, 0, 0)
    x, y, z = 0, 0, 0
    for i in range(n):
        x += points[i][0]
        y += points[i][1]
        z += points[i][2]
    return tuple(map(round, (x / n, y / n, z / n)))


def kmeans(rgb, k):
    n = len(rgb)

    # Initial random plots
    inits = [(random.randint(0, 255), random.randint(0, 255),
              random.randint(0, 255)) for _ in range(k)]

    # Representatives; avarage colors
    reps = inits
    # Which cluster color indexed i is in
    in_which = {i: 0 for i in range(n)}
    # How many times it trys to reach convergence
    loop = 30

    flag = True

    print("Converting...")

    for i in range(loop):
        clusters = {i: [] for i in range(k)}
        diff = 0
        for i in range(n):
            index = which_cluster(rgb[i], reps)
            clusters[index].append(rgb[i])
            in_which[i] = index
        for j in range(k):
            next_plot = avarage_color(clusters[j])
            for num in range(2):
                diff += abs(next_plot[num] - reps[j][num])
            reps[j] = next_plot
        if (diff < 50 * k and flag):
            print("Almost there...")
            flag = False
        if diff < 25 * k:
            break

    print("Finished !")
    return list(map(lambda x: reps[x], list(in_which.values())))
