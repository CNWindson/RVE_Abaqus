# -*- coding: utf-8 -*-
# author: Jiabo Wang
# QQ: 1457912352
# E-mail : 1457912352@qq.com
from abaqus import *
from abaqusConstants import *
from caeModules import *
import math
import random


def main(length, width, height, fiber_length, fiber_diameter, fiber_content):
    fiber_number = (length * width * height) * fiber_content / (fiber_length * math.pi * (fiber_diameter / 2))
    print("Fiber Number", fiber_number)
    part = mdb.models[mdb.models.keys()[0]].Part('Wrie')

    def get_end_point(x1, y1, z1, i1, j1, k1):
        vector_length = ((i1 ** 2 + j1 ** 2 + k1 ** 2) ** 0.5)
        scale = fiber_length / vector_length
        i2, j2, k2 = i1 * scale, j1 * scale, k1 * scale
        return x1 + i2, y1 + j2, z1 + k2

    fiber_number_finish = 0
    while fiber_number_finish < fiber_number:
        x_1 = random.uniform(0, length)
        y_1 = random.uniform(0, width)
        z_1 = random.uniform(0, height)
        i = random.uniform(-1, 1)
        j = random.uniform(-1, 1)
        k = random.uniform(-1, 1)
        x_2, y_2, z_2 = get_end_point(x_1, y_1, z_1, i, j, k)
        if 0 < x_2 < length and 0 < y_2 < width and 0 < z_2 < height:
            part.WirePolyLine(points=(((x_1, y_1, z_1), (x_2, y_2, z_2)),))
            fiber_number_finish += 1
    session.viewports[session.viewports.keys()[0]].setValues(displayedObject=part)
    print('Successful')


if __name__ == '__main__':
    length = float(getInput("length"))
    width = float(getInput("width"))
    height = float(getInput("height"))
    fiber_length = float(getInput("fiber_length"))
    fiber_diameter = float(getInput("fiber_diameter"))
    fiber_content = float(getInput("fiber_content"))
    main(length, width, height, fiber_length, fiber_diameter, fiber_content)
