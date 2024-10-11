from typing import Sequence
from PIL import Image
from color_mapper import ColorMapper


def generate_image(map: list[list[float]], min_height: float, max_height: float, file_path: str):

    width = 0
    height = 0

    color_mapper = ColorMapper(min_height, max_height)

    height = len(map)
    width = len(map[0])

    img = Image.new('L', (width, height))

    colors = flatten_map(color_mapper.map_colors(map))

    img.putdata(colors)
    img.save(file_path)


def flatten_map(map: list[list[int]]) -> list[int]:
    flat_list: list[int] = []

    for row in map:
        for cell in row:
            flat_list.append(cell)

    return flat_list
