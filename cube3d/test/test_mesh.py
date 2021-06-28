#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 08:43
# @Description: The data_graphics unittest script
#
#################################################
import unittest
from cube3d.data_model.tri4d import Tri4d
from cube3d.data_model.mesh import Mesh
from cube3d.data_model.point4d import Point4d

class TestMesh(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_cube_mesh(self):
        triangles: list[Tri4d] = []
        for _ in range(12):
            triangles.append(Tri4d([Point4d(), Point4d(), Point4d()]))
        cube_mesh = Mesh(triangles)
        self.assertTrue(len(cube_mesh.tri) == 12)


if __name__ == '__main__':
    unittest.main()
