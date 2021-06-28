#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 09:20
# @Description: The model factory test class
#
#################################################
import unittest
import numpy as np
from cube3d.data_model.model_factory import ModelFactory, Tri4d, Mesh

class TestModelFactory(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_make_point3d(self):
        pt = ModelFactory.point(x = 0, y = 0, z = 0)
        self.assertTrue(isinstance(pt, np.ndarray))
        self.assertTrue(pt.shape == (3, 1))

    def test_make_tri3d(self):
        vertices = []
        for _ in range(3):
            vertices.append(ModelFactory.point())
        tri3d = ModelFactory.tri3d(vertices)
        self.assertTrue(isinstance(tri3d, Tri4d))
        self.assertTrue(len(tri3d.vertices) == 3)

    def test_make_mesh(self):
        tri = []
        for _ in range(12):
            tri.append(ModelFactory.tri3d([ModelFactory.point() for _ in range(3)]))
        cube_mesh = ModelFactory.cube_mesh(tri)
        self.assertTrue(isinstance(cube_mesh, Mesh))
        self.assertTrue(len(cube_mesh.tri) == 12)


if __name__ == '__main__':
    unittest.main()
