from random import randint

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """A MemeEngine.

    It comprises an output path for the generated meme."""

    def __init__(self, output_dir: str):
        """Create a new 'MemeEngine'.

        Arguments:
            output_dir {str} -- path to which generated memes will be stored."""
        self._output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme.

        meme.make_meme(img_path, "It was a good dat today", "Michael").
        """

        with Image.open(img_path) as img:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            new_img = img.resize((width, height))

            draw = ImageDraw.Draw(new_img)
            font = ImageFont.truetype("./fonts/NotoSans/NotoSans-Bold.ttf")
            draw.text((10, 30), text + " " + author, font=font, fill="white")
            out_path = f"./_data/photos/memes/{randint(0, 10000)}.jpg"
            new_img.save(out_path)
            return out_path
