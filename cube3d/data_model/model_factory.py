#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 09:23
# @Description: The model factory class
#
#################################################
import numpy as np
from cube3d.data_model.tri4d import Tri4d
from cube3d.data_model.mesh import Mesh

class ModelFactory:

    @staticmethod
    def point(x: float = 0.0, y: float = 0.0, z: float = 0.0) -> np.array:
        return np.array([[x], [y], [z]])

    @staticmethod
    def tri3d(vertices: list[np.ndarray]) -> Tri4d:
        return Tri4d(vertices)

    @staticmethod
    def cube_mesh(triangles: list[Tri4d]) -> Mesh:
        return Mesh(triangles)
