import unittest
from utils.FileUtils import FileUtils
from utils.StringUtils import StringUtils
from utils.RectancleUtil import RectangleUtil
from utils.Configurations import *

import re
import sys
import allure
from datetime import datetime


class CoordinateTests(unittest.TestCase):

    def setUp(self):
        self.parent_directory = sys.path[0]

        self.file_reader = FileUtils()
        self.string_util = StringUtils()
        self.rec_util = RectangleUtil()
        self.input_file = get_input_file_path()
        self.output_file = get_output_file_path()
        self.report_file = get_rport_file_path()

        self.rec_coordinates = self.rec_util.get_rectangle_coordinates(
            self.parent_directory + self.input_file)

        self.output_coordinates = self.rec_util.get_visited_points_from_output_file(
            self.parent_directory + self.output_file)

        self.input_coordinates = self.rec_util.get_visited_points_from_input_file(
            self.parent_directory + self.input_file)

    # Reading the input file coordinates
    # Verify input coordinates are within the rectangle range
    # Write the results to a text file
    # Do a final assertions
    @allure.story('epic_input_coordinates')
    @allure.severity(allure.severity_level.MINOR)
    def test_input_coordinates_within_range(self):
        print('...starting......test_input_coordinates_within_range')
        results_file_name = self.parent_directory + self.report_file + 'test_input_coordinates_within_rangenow_' + str(
            datetime.now()) + '.txt'
        results = []
        for coordinate in self.input_coordinates:
            x = re.sub("[()]", "", coordinate).split(",")[0].strip()
            y = re.sub("[()]", "", coordinate).split(",")[1].strip()
            result = self.rec_util.is_inside_rectangle(self.rec_coordinates, float(x), float(y))
            if result:
                results.append(self.string_util.get_tupple_result(x, y, 'PASS'))
            else:
                results.append(self.string_util.get_tupple_result(x, y, 'FAIL'))
        self.file_reader.write_text_file(results_file_name, results)

        if [status for status in results if "FAIL" in status]:
            self.assertTrue(False, results)
        else:
            self.assertTrue(True, results)

    # Reading the out put file coordinates
    # Verify out put  coordinates are within the rectangle range
    # Write the results to a text file
    # Do a final assertions
    @allure.story('epic_output_coordinates')
    @allure.severity(allure.severity_level.MINOR)
    def test_output_coordinates_within_range(self):
        print('...starting......test_output_coordinates_within_range')
        results_file_name = self.parent_directory + self.report_file + 'test_output_coordinates_within_rangenow_' + str(
            datetime.now()) + '.txt'
        results = []
        for coordinate in self.output_coordinates:
            x = re.sub("[()]", "", coordinate).split(",")[0].strip()
            y = re.sub("[()]", "", coordinate).split(",")[1].strip()
            result = self.rec_util.is_inside_rectangle(self.rec_coordinates, float(x), float(y))
            if result:
                results.append(self.string_util.get_tupple_result(x, y, 'PASS'))
            else:
                results.append(self.string_util.get_tupple_result(x, y, 'FAIL'))
        self.file_reader.write_text_file(results_file_name, results)

        if [status for status in results if "FAIL" in status]:
            self.assertTrue(False, results)
        else:
            self.assertTrue(True, results)


if __name__ == '__main__':
    unittest.main()
