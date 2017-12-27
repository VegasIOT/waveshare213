import sys
import epd2in13
import time
import Image
import ImageDraw
import ImageFont
import textwrap

def main():
    epd = epd2in13.EPD()
    epd.init(epd.lut_full_update)

    text = textwrap.fill("test of the longest sentence you can write",width=12)


    # For simplicity, the arguments are explicit numerical coordinates
    # print("Width"+str(epd2in13.EPD_WIDTH))
    # print("Height"+str(epd2in13.EPD_HEIGHT))
    image = Image.new('1', (epd2in13.EPD_WIDTH,epd2in13.EPD_HEIGHT), 255)  # 255: clear the frame
    image2 = Image.new('1', (epd2in13.EPD_HEIGHT,epd2in13.EPD_WIDTH), 255)
    draw = ImageDraw.Draw(image2)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 30)
    draw.text((15, 15), text, font = font, fill = 0)

    

    # image.save("image.png")
    image2 = image2.rotate(270,expand=True)
    # image2.save("image2.png")
    
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image2, 0, 0)
    epd.display_frame()



if __name__ == '__main__':
    main()

