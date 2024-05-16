import imageio
import numpy as np


def image_to_binary_grid(image_path, grid_size=(100, 140), threshold=128):
    # Read the image using imageio
    image = imageio.imread(image_path, mode='L')  # Use mode='L' for grayscale

    # Get the dimensions of the image and the grid size
    height, width = image.shape
    grid_width, grid_height = grid_size

    # Calculate the size of each grid cell
    cell_width = width // grid_width
    cell_height = height // grid_height

    # Initialize the binary grid
    binary_grid = []

    # Iterate through each grid cell
    for y in range(grid_height):
        row = []
        for x in range(grid_width):
            # Get the region corresponding to the current grid cell
            region = image[y * cell_height: (y + 1) * cell_height,
                     x * cell_width: (x + 1) * cell_width]
            # Determine if the region is mostly black or white based on the threshold
            average = np.mean(region)
            if average < threshold:
                row.append(1)  # Black
            else:
                row.append(0)  # White
        binary_grid.append(row)

    return binary_grid


def print_binary_grid(binary_grid):
    # Print the binary grid without spaces
    for row in binary_grid:
        print('[{}]'.format(','.join(map(str, row))))


if __name__ == "__main__":
    # Path to the image file
    image_path = "your_image.jpg"

    # Define the grid size
    grid_size = (22, 22)

    # Define the threshold for black/white determination (0-255)
    threshold = 128

    # Convert the image to binary grid
    binary_grid = image_to_binary_grid(image_path, grid_size, threshold)

    # Print the binary grid
    print_binary_grid(binary_grid)
