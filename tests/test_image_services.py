from PIL import Image

from services.image_services import optimize_image


def test_optimize_image_resizes_large_image():
    image = Image.new("RGB", (2000, 1500))

    result = optimize_image(image)

    assert result.width <= 1080
    assert result.height <= 1080


def test_optimize_image_converts_rgba_to_rgb():
    image = Image.new("RGBA", (500, 500))

    result = optimize_image(image)

    assert result.mode == "RGB"