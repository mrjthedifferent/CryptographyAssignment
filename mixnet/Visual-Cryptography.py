import numpy as np
from PIL import Image

img = "images/kuet_logo.png"

I = np.array(Image.open(img).convert('CMYK')).astype(float)                       # Read and convert the image to CMYK color space

I = [I[::, ::, i] for i in range(3)]                                              # Separate the channels (Cyan, Magenta, Yellow) from the image


def halftone(I):                                                                  # Apply halftoning algorithm to each channel
    for i in range(2, len(I) - 2):
        for j in range(2, len(I[0]) - 2):                                         # Calculate the error between the current pixel value and the nearest color level (either 0 or 255)
            e = I[i][j] if I[i][j] < 128 else I[i][j] - 255                       # Set the pixel value to either 0 or 255 based on the error
            I[i][j] = 0 if I[i][j] < 128 else 255                                 # Spread the error to neighboring pixels using a predefined matrix

            I[i:i+3, j-2:j+3] += np.array([[0, 0, 0, 7, 5], [3, 5, 7, 5, 3], [1, 3, 5, 3, 1]]) / 48 * e

    return I[2:-2, 2:-2]                                                          # Return the halftoned image, excluding the padded borders

I = [halftone(np.pad(x, 2)) for x in I]                                           # Apply halftoning to each channel


S = [[np.zeros(2 * np.array(I[0].shape)) for _ in range(4)] for _ in range(2)]    # Create empty arrays for storing the halftone results


P = [np.array([[1, 0], [0, 1]]), np.array([[0, 1], [1, 0]])]                      # Define two pattern matrices


for n in range(3):                                                                # Iterate over the channels
    for i in range(I[0].shape[0]):                                                # Iterate over each pixel in the current channel
        for j in range(I[0].shape[1]):                                            # Randomly choose a pattern (0 or 1)
            p = np.random.randint(2)
            if I[n][i][j] == 255:                                                 # If the pixel value is 255 (white)
                S[p][n][i*2:i*2+2, j*2:j*2+2] = P[0]                              # Use pattern 0
                S[1-p][n][i*2:i*2+2, j*2:j*2+2] = P[1]                            # Use pattern 1
            else:                                                                 # If the pixel value is not 255 (black)
                S[p][n][i*2:i*2+2, j*2:j*2+2] = P[p]                              # Use pattern p
                S[1-p][n][i*2:i*2+2, j*2:j*2+2] = P[p]                            # Use pattern p

for i in range(2):                                                                # Convert the halftone results to the CMYK color space and save them as separate images
    S[i] = np.stack(S[i], -1).astype(np.uint8) * 255
    Image.fromarray(S[i], 'CMYK').save(f'mixnet/share{i+1}.jpg')

Image.fromarray(S[0] + S[1], 'CMYK').save('mixnet/result.jpg')                           # Combine the halftone results and convert them to the CMYK color space, then save the final image

