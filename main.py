import cv2
import numpy as np


def main():
    img1 = cv2.imread("patch_1.png")
    img2 = cv2.imread("patch_2.png")
    merged_img = np.concatenate((img1, img2), axis=1)
    cv2.imwrite("merged.png", merged_img)


if __name__ == "__main__":
    main()
