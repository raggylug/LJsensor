import numpy as np
from matplotlib import pyplot as plt
from src.my_package.plane_with_fitted_circle import plot_2d_plane_with_circle_and_point
from src.my_package.plot_2d_with_circle import plot_2d_plane_with_circle
from src.my_package.read_data import read_data, preprocess_data
from src.my_package.plot_3d import plot_3d_surface
from src.my_package.plot_2d import plot_2d_plane
from src.my_package.save_circle_centers import save_circle_centers_csv
from src.my_package.slice_plane_at_angle import process_csv_and_generate_coordinates, save_results_to_csv


def main():
    # Read original data
    file_path = r'C:\MLOptic\Keyence\LJ data\smartMTF1.csv'
    df = read_data(file_path)
    df_processed = preprocess_data(df)
    heights = (2.87 - df_processed.values) * 25400 / 12.5

    # Read upsampled data
    # file_path = r'C:\Python\LJsensor\src\upsampled_data.csv'
    # df = read_data(file_path)
    # df_processed = preprocess_data(df)
    # heights = (2.87 - df_processed.values) * 25400 / 6.25
    # upsample_y_and_x(df.values)

    # Create meshgrid
    x, y = range(1, heights.shape[1] + 1), range(1, heights.shape[0] + 1)
    x_grid, y_grid = np.meshgrid(x, y)

    # plot_3d_surface(x_grid, y_grid, heights, cmap='viridis')

    # plot_2d_plane(x_grid, heights, 10000)

    # plot_2d_plane_with_circle(x_grid, heights, 10000)

    # save_circle_centers_csv(x_grid, heights, range(9200, 10800))

    # Save 2d planes for MATLAB
    # csv_file_path = r'C:\Python\LJsensor\src\center_and_radius_of_circles_cone_12000_14000.csv'
    # results = process_csv_and_generate_coordinates(csv_file_path, heights, 0)
    # output_file_path = r'C:\Python\LJsensor\src\2Dplanes_12000_14000_0.csv'
    # save_results_to_csv(results, output_file_path)

    # point_to_plot = np.array([1739.6339637101842, 6893.5383722866145])
    # plot_2d_plane_with_circle_and_point(x_grid, heights, 14799, point_to_plot)

    # Load data for rotation
    # heights = np.load('heights_rotated_10.npy')
    # heights = heights.T

    # heights_rotated = plot_3d_rotate(heights, 10)
    # np.save('heights_rotated.npy', heights_rotated)


if __name__ == "__main__":
    main()
