#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 08:59
# @Description: The cube class
# @Source: https://www.youtube.com/watch?v=ih20l3pJoeU
#
#################################################
from __future__ import annotations
from cube3d.data_model.mesh import Mesh
from cube3d.data_model.tri4d import Tri4d
from cube3d.data_model.point4d import Point4d

def _init_cube(mesh: Mesh):
    if mesh is None:
        mesh = Mesh([
            # SOUTH
            Tri4d([Point4d(x = 0, y = 0, z = 0), Point4d(x = 0, y = 1, z = 0), Point4d(x = 1, y = 1, z = 0)]),
            Tri4d([Point4d(x = 0, y = 0, z = 0), Point4d(x = 1, y = 1, z = 0), Point4d(x = 1, y = 0, z = 0)]),
            # EAST
            Tri4d([Point4d(x = 1, y = 0, z = 0), Point4d(x = 1, y = 1, z = 0), Point4d(x = 1, y = 1, z = 1)]),
            Tri4d([Point4d(x = 1, y = 0, z = 0), Point4d(x = 1, y = 1, z = 0), Point4d(x = 1, y = 0, z = 1)]),
            # NORTH
            Tri4d([Point4d(x = 1, y = 0, z = 1), Point4d(x = 1, y = 1, z = 1), Point4d(x = 0, y = 1, z = 1)]),
            Tri4d([Point4d(x = 1, y = 0, z = 1), Point4d(x = 0, y = 1, z = 1), Point4d(x = 0, y = 0, z = 1)]),
            # WEST
            Tri4d([Point4d(x = 0, y = 0, z = 1), Point4d(x = 0, y = 1, z = 1), Point4d(x = 0, y = 1, z = 0)]),
            Tri4d([Point4d(x = 0, y = 0, z = 1), Point4d(x = 0, y = 1, z = 0), Point4d(x = 0, y = 0, z = 0)]),
            # TOP
            Tri4d([Point4d(x = 0, y = 1, z = 0), Point4d(x = 0, y = 1, z = 1), Point4d(x = 1, y = 1, z = 1)]),
            Tri4d([Point4d(x = 0, y = 1, z = 0), Point4d(x = 1, y = 1, z = 1), Point4d(x = 1, y = 1, z = 0)]),
            # BOTTOM
            Tri4d([Point4d(x = 1, y = 0, z = 1), Point4d(x = 0, y = 0, z = 1), Point4d(x = 0, y = 0, z = 0)]),
            Tri4d([Point4d(x = 1, y = 0, z = 1), Point4d(x = 0, y = 0, z = 0), Point4d(x = 1, y = 0, z = 0)]),
        ])
    return mesh

# ================================ CUBE CLASS ================================
class Cube:

    def __init__(self, mesh: Mesh = None):
        self.mesh = _init_cube(mesh)

    def __eq__(self, other: Cube) -> bool:
        return self.mesh == other.mesh

    def __hash__(self):
        return int(hash(self.mesh))
