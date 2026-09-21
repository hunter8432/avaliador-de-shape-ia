from PIL import Image


def optimize_image(image: Image.Image) -> Image.Image:
    image = image.copy()

    image.thumbnail((1080, 1080))

    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")

    return image