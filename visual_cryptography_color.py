import numpy as np
from PIL import Image


def halftone(I):
    """
    Convert an image to binary using halftoning
    :param I: Input image
    :return: Halftoned image
    """
    for i in range(2, len(I) - 2):
        # Calculate the error between the current pixel value and the nearest color level (either 0 or 255)
        for j in range(2, len(I[0]) - 2):
            # Set the pixel value to either 0 or 255 based on the error
            e = I[i][j] if I[i][j] < 128 else I[i][j] - 255
            # Spread the error to neighboring pixels using a predefined matrix
            I[i][j] = 0 if I[i][j] < 128 else 255

            I[i:i + 3, j - 2:j + 3] += np.array([[0, 0, 0, 7, 5], [3, 5, 7, 5, 3], [1, 3, 5, 3, 1]]) / 48 * e

    # Return the halftoned image, excluding the padded borders
    return I[2:-2, 2:-2]


def main():
    img = "images/kuet_logo.png"

    # Read and convert the image to CMYK color space
    I = np.array(Image.open(img).convert('CMYK')).astype(float)

    # Separate the channels (Cyan, Magenta, Yellow) from the image
    I = [I[::, ::, i] for i in range(3)]

    # Apply halftoning to each channel
    I = [halftone(np.pad(x, 2)) for x in I]

    # Create empty arrays for storing the halftone results
    S = [[np.zeros(2 * np.array(I[0].shape)) for _ in range(4)] for _ in range(2)]

    # Define two pattern matrices
    P = [np.array([[1, 0], [0, 1]]), np.array([[0, 1], [1, 0]])]

    # Iterate over the channels
    for n in range(3):
        # Iterate over each pixel in the current channel
        for i in range(I[0].shape[0]):
            # Randomly choose a pattern (0 or 1)
            for j in range(I[0].shape[1]):
                p = np.random.randint(2)
                # If the pixel value is 255 (white)
                if I[n][i][j] == 255:
                    S[p][n][i * 2:i * 2 + 2, j * 2:j * 2 + 2] = P[0]  # Use pattern 0
                    S[1 - p][n][i * 2:i * 2 + 2, j * 2:j * 2 + 2] = P[1]  # Use pattern 1
                else:  # If the pixel value is not 255 (black)
                    S[p][n][i * 2:i * 2 + 2, j * 2:j * 2 + 2] = P[p]  # Use pattern p
                    S[1 - p][n][i * 2:i * 2 + 2, j * 2:j * 2 + 2] = P[p]  # Use pattern p

    # Convert the halftone results to the CMYK color space and save them as separate images
    for i in range(2):
        S[i] = np.stack(S[i], -1).astype(np.uint8) * 255
        Image.fromarray(S[i], 'CMYK').save(f'outputs/share{i + 1}.jpg')

    # Combine the halftone results and convert them to the CMYK color space, then save the final image
    Image.fromarray(S[0] + S[1], 'CMYK').save('outputs/result.jpg')

    # Show the images
    Image.open("outputs/share1.jpg").show()
    Image.open("outputs/share2.jpg").show()
    Image.open("outputs/result.jpg").show()


if __name__ == '__main__':
    main()
