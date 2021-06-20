#coding: utf-8
from PIL import Image, ImageFont, ImageDraw

def char_size():
    return 20


def text_2_image(text_in,font_in):
    height = char_size()
    width = len(text_in) * char_size() + char_size()
    pil_image = Image.new("RGBA", (width,height), 'black')

    draw = ImageDraw.Draw(pil_image)
    text_width, text_height = draw.textsize(text_in,font=my_font)
    draw.text(((width/2)-(text_width/2), (height/2 - 2)-(text_height/2)), text_in, "white", font=font_in)
    return pil_image

my_font = ImageFont.truetype("./Noto_Sans_HK/NotoSansHK-Light.otf", char_size())

my_image = text_2_image(u'阿爺有冇踩單車?', my_font)
# my_image = text_2_image(u'阿爸,食咗飯未?', my_font)
# my_image = text_2_image(u'今個星期有冇出街?', my_font)
# my_image = text_2_image(u'今日有冇出街?', my_font)
# my_image = text_2_image(u'阿爸,喺屋企做多啲運動啦!', my_font)
# my_image = text_2_image(u'阿爸,可以落街行下', my_font)
# my_image = text_2_image(u'阿爸,有冇食麥當勞?', my_font)
# my_image = text_2_image(u'唔好飲咁多汽水,可以飲果汁呀.', my_font)
# my_image = text_2_image(u'今日食咗乜嘢?', my_font)
# my_image = text_2_image(u'今日食咗乜嘢?', my_font)
my_image.show()
my_image.save('new_image.ppm')
