#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 08:49
# @Description: The Mesh class
# @Source: https://www.youtube.com/watch?v=ih20l3pJoeU
#
#################################################
from __future__ import annotations
from cube3d.data_model.tri4d import Tri4d

class Mesh:

    def __init__(self, triangles: list[Tri4d]):
        self.tri = triangles

    def __eq__(self, other: Mesh) -> bool:
        return all([self.tri[i] == other.tri[i] for i in range(len(self.tri))])

    def __hash__(self):
        h = 0
        for t in self.tri:
            h += hash(t)
        return int(h)
