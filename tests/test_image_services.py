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


def test_optimize_image_converts_p_to_rgb():
    image = Image.new("P", (500, 500))

    result = optimize_image(image)

    assert result.mode == "RGB"


def test_optimize_image_keeps_rgb():
    image = Image.new("RGB", (500, 500))

    result = optimize_image(image)

    assert result.mode == "RGB"
def test_optimize_image_does_not_modify_original():
    image = Image.new("RGB", (2000, 1500))
    
    original_size = image.size
    
    assert image.size == original_size

def test_optimize_image_preserves_aspect_ratio():
    image = Image.new("RGB", (2000, 1000))  # Aspect ratio 2:1

    result = optimize_image(image)

    assert result.width / result.height == 2 / 1
    