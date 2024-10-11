"""Generates a two dimensional height map"""

import argparse
from height_map_generator import HeightMapGenerator
from image_generator import generate_height_map_image

DEFAULT_X_AXIS_LENGTH = 100
DEFAULT_Y_AXIS_LENGTH = 100
DEFAULT_MIN_HEIGHT = 0
DEFAULT_MAX_HEIGHT = 100
DEFAULT_RANDOM_SCALE = 75


def main(x_axis_length: int, y_axis_length, min_height: float, max_height: float, random_scale: float, file_path: str):

    generator = HeightMapGenerator(
        x_axis_length, y_axis_length, min_height, max_height, random_scale)

    map = generator.generate_height_map()

    generate_height_map_image(map, min_height, max_height, file_path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='HeightMapGenerator',
        description='Generates a height map'
    )

    parser.add_argument('-x', '--x-axis-length', default=DEFAULT_X_AXIS_LENGTH,
                        help=f'The length of the x-axis. Default value is {DEFAULT_X_AXIS_LENGTH}.', required=False, type=int)

    parser.add_argument('-y', '--y-axis-length', default=DEFAULT_Y_AXIS_LENGTH,
                        help=f'The length of the y-axis. Default value is {DEFAULT_X_AXIS_LENGTH}.', required=False, type=int)

    parser.add_argument('-m', '--min-height', default=DEFAULT_MIN_HEIGHT,
                        help='The minimum height allowed.', required=False, type=float)

    parser.add_argument('-M', '--max-height', default=DEFAULT_MAX_HEIGHT,
                        help='The maximum height allowed.', required=False, type=float)

    parser.add_argument('-r', '--random-scale', default=DEFAULT_RANDOM_SCALE,
                        help='A number used to generate random height differences. The larger the number the larger the differences.', required=False, type=float)

    parser.add_argument(
        '-f', '--out-file-path', help='The file to output the height map to.', required=True, type=str)

    args = parser.parse_args()

    main(args.x_axis_length, args.y_axis_length, args.min_height,
         args.max_height, args.random_scale, args.out_file_path)
