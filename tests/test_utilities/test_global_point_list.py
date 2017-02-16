# -*- coding: utf-8 -*-
from numpy import array
from numpy.testing import assert_allclose

from pysimplevtk.utilities import GlobalPointList


class TestGetPointId(object):

    def test_GivenNoPreviousPoint_AddPointAndReturnID(self):
        global_point_list = GlobalPointList()
        point = array([0, 0, 0])
        point_id = global_point_list.get_point_id(point)
        assert point_id == 0
        assert_allclose(global_point_list.points, array([[0, 0, 0]]))

    def test_GivenTheSamePreviousPoint_ReturnID(self):
        global_point_list = GlobalPointList()
        point = array([0, 0, 0])
        _ = global_point_list.get_point_id(point)
        point_id = global_point_list.get_point_id(point)
        assert point_id == 0
        assert_allclose(global_point_list.points, array([[0, 0, 0]]))

    def test_GivenTheOtherPreviousPoint_AddPointAndReturnID(self):
        global_point_list = GlobalPointList()
        point = array([0, 0, 0])
        _ = global_point_list.get_point_id(point)
        point = array([1, 1, 1])
        point_id = global_point_list.get_point_id(point)
        assert point_id == 1
        assert_allclose(
            global_point_list.points,
            array([[0, 0, 0], [1, 1, 1]]))
