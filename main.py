from get_tex import get_tex
from amend_tex import amend_tex
import cv2


def main(img: cv2.Mat):
    tex = get_tex(img)
    print(tex)

    amended_tex = amend_tex(tex)
    print(amended_tex)

    return amended_tex


if __name__ == "__main__":
    img = cv2.imread("test.png")
    print(main(img))
