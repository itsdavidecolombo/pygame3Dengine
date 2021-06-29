#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 11:15
# @Description: A class for applying mathematical operations on the data structures
#
#################################################
import math
import numpy as np
import logging
from cube3d.data_model.tri4d import Tri4d, Point4d
from cube3d.ui import Window

class Transformer:
    Z_NEAR: float = 0.1
    Z_FAR: float  = 1000.0
    FOV_ANGLE_DEG: float = 90.0
    FOV_RADIANS: float   = 1.0 / math.tan((FOV_ANGLE_DEG / 2) / 180.0 * math.pi)
    ASPECT_RATIO: float  = float(Window.DEFAULT_HEIGHT) / float(Window.DEFAULT_WIDTH)
    PROJECTION_MATRIX: np.ndarray

    @staticmethod
    def set_fov_angle_degree(angle_degree: float):
        Transformer.FOV_ANGLE_DEG = angle_degree
        Transformer.__set_fov_radians()

    @classmethod
    def __set_fov_radians(cls):
        cls.FOV_RAD = 1.0 / math.tan((cls.FOV_ANGLE_DEG / 2) / 180.0 * math.pi)

    @staticmethod
    def set_aspect_ratio(aspect: float):
        if aspect == 0.0:
            logging.log(level = logging.ERROR, msg = f'Aspect ratio is zero')
            raise ValueError(f'Aspect ratio is equal to zero')
        Transformer.ASPECT_RATIO = 1 / aspect

    @staticmethod
    def set_z_near(z_near: float):
        Transformer.Z_NEAR = z_near

    @staticmethod
    def set_z_far(z_far: float):
        Transformer.Z_FAR = z_far

    @staticmethod
    def update_projection_matrix():
        Transformer.PROJECTION_MATRIX = Transformer.__projection_mat()

    @classmethod
    def __projection_mat(cls):
        return np.array([
            [cls.ASPECT_RATIO*cls.FOV_RADIANS, 0, 0, 0],
            [0, cls.FOV_RADIANS, 0, 0],
            [0, 0, cls.Z_FAR / (cls.Z_FAR - cls.Z_NEAR), -cls.Z_NEAR*cls.Z_FAR / (cls.Z_FAR - cls.Z_NEAR)],
            [0, 0, 1, 0]
        ])

# ============================== SCALE METHOD ==============================
    @staticmethod
    def scale_tri(obj4d: Tri4d, scaling: np.array) -> Tri4d:
        new_v = [Transformer.__multiply_matrix_vec4d(vec4d = v.point, mat = scaling) for v in obj4d.vertices]
        return Tri4d(new_v)

# ============================== PROJECTION ==============================
    @staticmethod
    def project_tri(obj4d: Tri4d) -> Tri4d:
        new_v = [Transformer.__multiply_matrix_vec4d(vec4d = v.point, mat = Transformer.PROJECTION_MATRIX) for v in obj4d.vertices]
        return Tri4d(new_v)

    @classmethod
    def __multiply_matrix_vec4d(cls, vec4d: np.ndarray, mat: np.ndarray) -> Point4d:
        proj_vec4d = np.dot(mat, vec4d)
        if proj_vec4d[3][0] != 0:
            proj_vec4d /= proj_vec4d[3][0]
        return Point4d(x = proj_vec4d[0][0], y = proj_vec4d[1][0], z = proj_vec4d[2][0], t = 1.0)
