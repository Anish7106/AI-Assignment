import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import time
import sys

WIDTH = 220
HEIGHT = 100
CAPTCHA_LENGTH = 6


def generate_captcha_text(length=CAPTCHA_LENGTH):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))


def add_noise(draw):
    for _ in range(2):
        draw.line(
            (
                random.randint(0, WIDTH),
                random.randint(0, HEIGHT),
                random.randint(0, WIDTH),
                random.randint(0, HEIGHT)
            ),
            fill="lightgray",
            width=1
        )

    for _ in range(30):
        draw.point(
            (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
            fill="gray"
        )


def generate_captcha_image(text):
    image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    for i, char in enumerate(text):
        x = 30 + i * 25 + random.randint(-3, 3)
        y = 35 + random.randint(-5, 5)
        draw.text((x, y), char, font=font, fill="black")

    add_noise(draw)

    image = image.filter(ImageFilter.SMOOTH)

    filename = "captcha_image.png"
    image.save(filename)
    return filename


def open_image(filename):
    if sys.platform.startswith("win"):
        os.startfile(filename)
    else:
        os.system(f'open "{filename}" 2>/dev/null || xdg-open "{filename}" 2>/dev/null')


def main():
    print("Generating CAPTCHA...\n")

    captcha_text = generate_captcha_text()
    image_file = generate_captcha_image(captcha_text)

    open_image(image_file)

    user_input = input("Enter CAPTCHA text: ").strip()

    if user_input == captcha_text:
        print("✅ Correct!")
    else:
        print("❌ Incorrect!")
        print("Correct answer was:", captcha_text)


main()