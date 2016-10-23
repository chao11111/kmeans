import math
import random
import numpy as np
INF = 1e10

class Kmeans:

    def __init__(self, K):
        self.K = K

    def compress(self, rgb, loop=30, alpha=50, monitor=True):
        N = len(rgb)
        inits = [np.random.random_integers(0, 255, 3) for _ in range(self.K)]
        reps = inits
        # Which cluster is an i-th element in ?
        label = {i: 0 for i in range(N)}
        print("Converting...")

        for i in range(loop):
            clusters = {i: [] for i in range(self.K)}
            # (1) Assignment Step
            for i in range(N):
                index = self.assign(rgb[i], reps)
                clusters[index] += [rgb[i]]
                label[i] = index
            # (2) Update Step
            diff = 0
            for j in range(self.K):
                centroid = self.average(clusters[j])
                diff += np.linalg.norm(centroid - reps[j])
                reps[j] = centroid
            if (diff < alpha * self.K and monitor):
                print("Almost there...")
                monitor = False
            if diff < alpha / 2 * self.K:
                break

        print("Finished !")
        out = map(lambda x: tuple(map(int,reps[x])), list(label.values()))
        return list(out)

    @staticmethod
    def assign(p, reps):
        N = len(reps)
        minimum = INF
        for i in range(N):
            dst = np.linalg.norm(p - reps[i])
            if minimum > dst:
                minimum = dst
                index = i
        return index

    @staticmethod
    def average(points):
        N = len(points)
        if N==0:
            return np.random.random_integers(0, 255, 3)
        else:
            avr = np.array([0, 0, 0])
            for p in points:
                avr += p
            return np.rint(avr / N)
