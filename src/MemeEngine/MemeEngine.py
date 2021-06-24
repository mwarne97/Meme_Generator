"""MemeEngine creates memes through the use of the 'Pillow' dependency."""
from random import randint

from PIL import Image, ImageDraw, ImageFont
import textwrap


class MemeEngine:
    """A MemeEngine.

    It comprises an output path for the generated meme.
    """

    def __init__(self, output_dir: str):
        """Create a new 'MemeEngine'."""
        self._output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme."""
        with Image.open(img_path) as img:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            new_img = img.resize((width, height))

            draw = ImageDraw.Draw(new_img)
            font = ImageFont.truetype("./fonts/NotoSans/NotoSans-Bold.ttf")
            wrapped_text = textwrap.fill(text=f"{text} - {author}")
            draw.text((10, 30), wrapped_text, font=font, fill="white")

            # .png extension converts both .png and .jpg image files
            out_path = f"./static/{randint(0, 10000)}.png"
            new_img.save(out_path)
            return out_path
