import re
from utils.FileUtils import FileUtils

class RectangleUtil:
    file_reader = FileUtils()

    def is_inside_rectangle(self, coordinates, x, y):
        x1 = coordinates[0]
        y1 = coordinates[1]
        y2 = coordinates[3]
        x2 = coordinates[4]

        result = (((x2 > x > x1) or (x1 > x > x2)) and ((y2 > y > y1) or (y1 > y > y2)))
        return result

    def get_rectangle_coordinates(self, file_path):
        contents = self.file_reader.read_text_file(file_path)
        temp = re.findall('-?\d+', contents[0:2][1])
        res = list(map(int, temp))
        return res

    def get_visited_points_from_input_file(self, file_path):
        contents = self.file_reader.read_text_file(file_path)
        new_lst = [x[:-1] for x in contents]
        formatted_list = new_lst[new_lst.index('Points') + 1:len(new_lst)]
        return formatted_list

    def get_visited_points_from_output_file(self, file_path):
        contents = self.file_reader.read_text_file(file_path)
        new_lst = [x[:-1] for x in contents]
        return new_lst
