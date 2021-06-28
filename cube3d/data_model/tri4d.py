#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:28
# @Description: The Tri3d data model class
#
#################################################
from __future__ import annotations
from cube3d.data_model.point4d import Point4d

class Tri4d:

    def __init__(self, vertices: list[Point4d]):
        if len(vertices) != 3:
            raise ValueError(f'A triangle must have three vertices: number of vertices passed = {len(vertices)}')
        self.vertices = vertices

    def __eq__(self, other: Tri4d) -> bool:
        return all([self.vertices[i] == other.vertices[i] for i in range(len(self.vertices))])

    def __hash__(self):
        h = 0
        for v in self.vertices:
            h += hash(v)
        return int(h)
