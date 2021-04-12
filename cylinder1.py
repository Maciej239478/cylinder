import random as rnd
from csv import writer
import numpy as np


def generate_cylinder(num_points: int = 10000, r=100, h=300):
    xx = []
    yy = []
    zz = []
    while (len(xx) < num_points):
        x = rnd.uniform(-1, 1) * r
        y = rnd.uniform(-1, 1) * np.sqrt(r ** 2 - x ** 2)
        z = rnd.uniform(-1, 1) * h

        xx.append(x)
        yy.append(y)
        zz.append(z)

    return zip(xx, yy, zz)


if __name__ == '__main__':
    cloud_points = generate_cylinder()
    with open('cylinder.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for p in cloud_points:
            csvwriter.writerow(p)
