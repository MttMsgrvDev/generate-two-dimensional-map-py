import sys
from height_map_generator import HeightMapGenerator
from image_generator import generate_image


def main(x_axis_length: int, y_axis_length, min_height: float, max_height: float, random_scale: float, file_path: str):

    generator = HeightMapGenerator(
        x_axis_length, y_axis_length, min_height, max_height, random_scale)

    map = generator.generate_height_map()

    generate_image(map, min_height, max_height, file_path)


if __name__ == "__main__":

    x_axis_length = int(sys.argv[1])

    y_axis_length = int(sys.argv[2])

    min_height = float(sys.argv[3])

    max_height = float(sys.argv[4])

    random_scale = float(sys.argv[5])

    file_path = sys.argv[6]

    main(x_axis_length, y_axis_length, min_height,
         max_height, random_scale, file_path)
