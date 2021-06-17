from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """"""
    def __init__(self, output_dir: str):
        """"""
        self._output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """"""
        with Image.open(img_path) as img:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            new_img = img.resize((width, height))

            draw = ImageDraw.Draw(new_img)
            font = ImageFont.truetype("./src/fonts/NotoSans/NotoSans-Bold.ttf")
            draw.text((10, 30), text + " " + author, font=font, fill="white")
            new_img.save(img_path)
            return img_path
