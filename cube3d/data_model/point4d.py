#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 06:44
# @Description: The 3d point class
#
#################################################
from __future__ import annotations
import numpy as np

class Point4d:

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, t: float = 1.0):
        self.point = np.array([[x], [y], [z], [t]])

    def __eq__(self, other: Point4d) -> bool:
        return (self.point == other.point).all()

    def __hash__(self):
        return int(np.sum(self.point))
