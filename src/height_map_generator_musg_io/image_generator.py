"""Contains functions needed to generate a height map image.

Functions
---------

generate_height_map_image:
    Generates an image file given a height map, the minimum height, the maximum height, and the path of the output file.

"""

from PIL import Image
from color_mapper import ColorMapper
from height_map import HeightMap


def generate_height_map_image(map: HeightMap, file_path: str):
    """Generates an image for a given height map.

    :param map: The height map to generate the image for.
    :type map: HeightMap

    :param min_height: The minimum height of the height map.
    :type min_height: float

    :param max_height: The maximum height of the height map.
    :type max_height: float

    :param file_path: The path to the image file to be generated.
    :type file_path: str
    """

    color_mapper = ColorMapper(map.min_height, map.max_height)

    img = Image.new('L', (map.x_axis_length, map.y_axis_length))

    colors = __flatten_map(color_mapper.map_colors(map))

    img.putdata(colors)
    img.save(file_path)


def __flatten_map(map: HeightMap) -> list[int]:
    flat_list: list[int] = []

    for y in range(map.y_axis_length):
        for x in range(map.x_axis_length):
            flat_list.append(map.get_height(x, y))

    return flat_list
