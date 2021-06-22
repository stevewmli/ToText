#coding: utf-8
import speech_recognition as sr
from PIL import Image, ImageFont, ImageDraw
r = sr.Recognizer()

def char_size():
    return 16


def text_2_image(text_in,font_in):
    height = char_size()
    width = len(text_in) * char_size() + char_size()
    pil_image = Image.new("RGBA", (width,height), 'black')

    draw = ImageDraw.Draw(pil_image)
    text_width, text_height = draw.textsize(text_in,font=my_font)
    draw.text(((width/2)-(text_width/2), (height/2 - 3)-(text_height/2)), text_in, "white", font=font_in)
    return pil_image

my_font = ImageFont.truetype("./Noto_Sans_HK/NotoSansHK-Light.otf", char_size())

# from microphone
with sr.Microphone() as source:
    print("Capturing...")
    audio = r.listen(source)

my_image = text_2_image(r.recognize_google(audio, language='yue'), my_font)
my_image.save('new_image.ppm')
