from PIL import Image, ImageDraw, ImageFont
import os

index_dir = "Исходные"
final_dir = "Готовые"

footer = Image.open('footer.png')
images = filter(lambda x: x.endswith(".jpg"), os.listdir(index_dir))

for image_file in images:
    name = image_file.split('.')[0];
    print(name)
    image = Image.open(index_dir + "/" + image_file)

    if (image.width >= int(image.height / 210 * 148) ):
        new_width = int(image.height / 210 * 148)
        offset = int((image.width - new_width ) / 2)
        image = image.crop([offset, 0, new_width+offset, image.height])
        print(new_width, "x", image.height, end="\n\n")
    else:
        new_height = int(image.width / 148 * 210)
        image = image.crop([0, 0, image.width, new_height])
        print(image.width, "x", new_height, end="\n\n")

    image = image.resize((993, 1405));

    image.paste(footer, (0, image.height-footer.height),  footer)
    
    draw = ImageDraw.Draw(image)

    if (len(name) > 19):
        font = ImageFont.truetype("Jikharev.ttf", 72)
    if (len(name) > 18):
        font = ImageFont.truetype("Jikharev.ttf", 76)
    elif (len(name) > 17):
        font = ImageFont.truetype("Jikharev.ttf", 82)
    else:
        font = ImageFont.truetype("Jikharev.ttf", 88)

    draw.text((240, image.height-175), name, font=font, fill=(0, 0, 254))
    del draw

    paper = Image.new("RGBA", (993*2+1, 1405), (255, 255, 255, 0))
    paper.paste(image, (0, 0))
    paper.paste(image, (994, 0))

    paper.save(final_dir + "/" + image_file, "JPEG")

# A5 - 148x210
# A4 - 210x297