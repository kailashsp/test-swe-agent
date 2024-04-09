import numpy as np
from PIL import Image


def main():
    img1 = Image.open("patch_1.png")
    img2 = Image.open("patch_2.png")
    merged_img = np.concatenate((img1, img2), axis=1)
    merged_img.save("merged.png", merged_img)


if __name__ == "__main__":
    main()
