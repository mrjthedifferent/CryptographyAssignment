from PIL import Image
import random


def pattern1(image, x, y):
    image.putpixel((x * 2, y * 2), 255)
    image.putpixel((x * 2 + 1, y * 2), 0)
    image.putpixel((x * 2, y * 2 + 1), 0)
    image.putpixel((x * 2 + 1, y * 2 + 1), 255)


def pattern2(image, x, y):
    image.putpixel((x * 2, y * 2), 0)
    image.putpixel((x * 2 + 1, y * 2), 255)
    image.putpixel((x * 2, y * 2 + 1), 255)
    image.putpixel((x * 2 + 1, y * 2 + 1), 0)


def combine_image(share1, share2):
    outfile = Image.new('1', share1.size)

    for x in range(share1.size[0]):
        for y in range(share1.size[1]):
            outfile.putpixel((x, y), max(
                share1.getpixel((x, y)), share2.getpixel((x, y))))

    return outfile


def main():
    image = Image.open('images/kuet.jpg')
    image = image.convert('1')

    share1 = Image.new("1", [dimension * 2 for dimension in image.size])
    share2 = Image.new("1", [dimension * 2 for dimension in image.size])

    for x in range(0, image.size[0], 2):
        for y in range(0, image.size[1], 2):
            sourcepixel = image.getpixel((x, y))
            assert sourcepixel in (0, 255)
            randomValue = random.random()
            if sourcepixel == 0:
                if randomValue < .5:
                    pattern1(share1, x, y)
                    pattern2(share2, x, y)
                else:
                    pattern2(share1, x, y)
                    pattern1(share2, x, y)

            elif sourcepixel == 255:
                if randomValue < .5:
                    pattern1(share1, x, y)
                    pattern1(share2, x, y)
                else:
                    pattern2(share1, x, y)
                    pattern2(share2, x, y)

    outfile = combine_image(share1, share2)
    share1.save('outputs/share1_bw.png')
    share2.save('outputs/share2_bw.png')
    outfile.save('outputs/result_bw.png')

    share1.show()
    share2.show()
    outfile.show()


if __name__ == '__main__':
    main()
