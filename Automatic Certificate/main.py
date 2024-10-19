from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from PIL import Image,ImageDraw,ImageFont
from fastapi.responses import FileResponse

app = FastAPI()


class CongLaoItem(BaseModel):
    text: str
    rank: str


@app.post("/quangteo")
def conglao(item: CongLaoItem):

    text = item.text
    rank = item.rank
    image =  Image.open("cert2_.png")


    d = ImageDraw.Draw(image)
    font = ImageFont.truetype("Pacifico-Bold.ttf", 100)
    font_rank = ImageFont.truetype("arial.ttf", 100)

    text_bbox = d.textbbox((0, 0), text, font=font)  # (x1, y1, x2, y2)
    rank_bbox = d.textbbox((0, 0), rank, font=font_rank)

    # Tính kích thước văn bản
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    rank_width = rank_bbox[2] - rank_bbox[0]
    rank_height = rank_bbox[3] - rank_bbox[1]

    img_width, img_height = image.size

    coord = ((img_width - text_width) // 2, 594)
    coord_rank = ((1000 - rank_width // 2), 984)
    color = (255, 255, 255)
    color_rank = (0, 0, 0)
    d.text(coord, text = text, fill = color, font = font)
    d.text(coord_rank, text = rank, fill = color_rank, font = font_rank)

    image.save(f"{text}_img.png")
    return FileResponse(f"{text}_img.png")