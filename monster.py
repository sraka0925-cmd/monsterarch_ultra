#!/usr/bin/env python3
"""Static image renderer. No animation, no refresh loop."""
import pathlib
import shutil
import sys
from PIL import Image

def run():
    path = pathlib.Path(__file__).with_name("monster.png")
    if not path.exists():
        path = pathlib.Path(sys.prefix)/"share/monster-ultra/monster.png"
    cols, rows = shutil.get_terminal_size((80, 35))
    image = Image.open(path).convert("RGB")
    width = max(4, min(cols-2, int((rows-4)*2*image.width/image.height)))
    height = max(2, int(width*image.height/image.width))
    height += height % 2
    image = image.resize((width, height), Image.Resampling.LANCZOS)
    lines = []
    pad = " " * max(0, (cols-width)//2)
    for y in range(0, height, 2):
        line = pad
        for x in range(width):
            a, b = image.getpixel((x,y)), image.getpixel((x,y+1))
            line += "\033[38;2;%d;%d;%dm\033[48;2;%d;%d;%dm▀" % (*a,*b)
        lines.append(line+"\033[0m")
    print("\n".join(lines))

if __name__ == "__main__":
    run()

