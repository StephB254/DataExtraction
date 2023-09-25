#!/usr/bin/python3

import cv2
from adv_spellcheck import SpellChecker

def load_image(image_path):
    img = cv2.imread(image_path)
    return img


def enhance_image(img):
    img = cv2.convertScaleAbs(img, alpha=1.5, beta=0) # Increase contrast
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21) # Denoise image
    img = cv2.GaussianBlur(img, (3, 3), 0) # Blur image to reduce noise
    return img


def divide_enlarge_image(img):
    height, width, channels = img.shape
    left_img = img[0:height, 0:int(width/2)]
    right_img = img[0:height, int(width/2):width]
    left_img = cv2.resize(left_img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    right_img = cv2.resize(right_img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    return left_img, right_img


def convert_to_grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def increase_intensity(img):
    img = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
    return img


def reduce_noise(img):
    img = cv2.fastNlMeansDenoising(img, None, 10, 7, 21)
    return img


def adaptive_threshold(img):
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return img


def apply_morphology(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return img


def extract_text(img):

    # Run Tesseract OCR on the image
    text = pytesseract.image_to_string(thresh, lang=lang)


def spell_check(text):
    # Code for spell-checking algorithm goes here
    SpellChecker(vocab_path)
    pass


def save_text(text, file_path):
    with open(file_path, 'w') as f:
        f.write(text)




###########################################################################

import pytesseract
import cv2

def extract_text(image_path, lang='eng'):
    # Load image using OpenCV
    img = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to improve contrast
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Run Tesseract OCR on the image
    text = pytesseract.image_to_string(thresh, lang=lang)

    return text
