#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 20:13
# @Description: The Transformer unittest script
#
#################################################
import unittest
import numpy as np
from cube3d.utils.transformer import Transformer, Tri4d, Point4d

class TestTransformer(unittest.TestCase):

    def setUp(self) -> None:
        self.vertices: list[Point4d] = []
        self.vertices.append(Point4d(x = 1, y = 0, z = 0))
        self.vertices.append(Point4d(x = 0, y = 1, z = 0))
        self.vertices.append(Point4d(x = -1, y = 0, z = 0))
        self.tri = Tri4d(self.vertices)

    def tearDown(self) -> None:
        pass

    def test_scale_tri(self):
        scale_x = 2
        scale_y = 2
        scale_z = 0
        scaling = np.array([[scale_x, 0, 0, 0], [0, scale_y, 0, 0], [0, 0, scale_z, 0], [0, 0, 0, 1]])
        self.tri = Transformer.scale_tri(self.tri, scaling)
        i = 0
        for v in self.vertices:
            self.assertTrue((self.tri.vertices[i].point == np.dot(scaling, v.point)).all())
            i += 1

    def test_project_tri4d(self):
        Transformer.set_aspect_ratio(800/600)
        Transformer.update_projection_matrix()
        self.tri = Transformer.project_tri(self.tri)
        i = 0
        for v in self.vertices:
            dot = np.dot(Transformer.PROJECTION_MATRIX, v.point)
            self.assertTrue(dot.shape == (4, 1))
            if dot[3][0] != 0:
                dot /= dot[3][0]
            dot = np.array([[dot[0][0]], [dot[1][0]], [dot[2][0]], [1.0]])
            self.assertTrue((self.tri.vertices[i].point == dot).all())
            i += 1


if __name__ == '__main__':
    unittest.main()
