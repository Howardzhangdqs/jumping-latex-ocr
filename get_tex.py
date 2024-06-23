from PIL import Image
from pix2tex.cli import LatexOCR
import cv2


model = LatexOCR()


def get_tex(img: cv2.Mat):
    img = Image.fromarray(img)
    return model(img)
