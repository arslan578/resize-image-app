from pathlib import Path
from PIL import ImageFont, ImageDraw, Image, ImageSequence
import uuid
import cv2
import imageio
import sys
from imgpy import Img

BASIC_DIR = str(Path(__file__).resolve().parent) + '/static/'

"""
    ('new-width', '280'),
     ('new-height', '122'), 
     ('unit', 'percentage'), 
     ('fnl-image-format', 'png'), 
     ('quality', '12'), 
     ('bg-color', 'black')])


"""


def image_processing(data, request):
    try:

        get_user_file = request.files['resize-file']
        save_user_image_path = BASIC_DIR + 'media/user_images/{file_name}'.format(
            file_name=request.files['resize-file'].filename)
        get_user_file.save(save_user_image_path)
        if '.gif' in request.files['resize-file'].filename and data.get('fnl-image-format', '') == 'gif':
            url = resize_gif(data, save_user_image_path)
        elif data.get('fnl-image-format', 'png') in ['png', 'jpg', 'jpeg']:
            url = jpg_to_png_and_vise_versa(data, save_user_image_path)
        else:
            white_image = BASIC_DIR + 'media/bg_images/custom_white_image.jpg'
            url = jpg_png_to_gif(data, save_user_image_path, white_image)

        return url
    except Exception as e:
        pass


def get_units(data):
    width = int(data.get('new-width', '0'))
    height = int(data.get('new-height', '0'))
    unit = data.get('unit', '')
    if unit == 'percentage':
        width = int(width * 6.25)
        height = int(height * 6.25)

    return width, height


def get_file_name(data):
    file_final_format = data.get('fnl-image-format', 'png')
    save_resize_image_url = 'media/resize_images/{new_file_name}.{file_format}'.format(
        new_file_name=str(uuid.uuid4()).replace('-', '_'), file_format=file_final_format)
    save_resize_image = BASIC_DIR + save_resize_image_url

    return save_resize_image_url, save_resize_image


def jpg_to_png_and_vise_versa(data, save_user_image_path):
    width, height = get_units(data)
    quality = int(data.get('quality')) if data.get('quality') != '' else 100
    save_resize_image_url, save_resize_image = get_file_name(data)
    image = Image.open(save_user_image_path)
    resize_image = image.resize((width, height), Image.ANTIALIAS)
    try:
        resize_image.save(save_resize_image, quality=quality)
    except OSError:

        resize_image = image.convert('RGB')
        resize_image.save(save_resize_image, quality=quality)

    if data['bg-color'] in ['black', 'white']:
        if data['bg-color'] == 'white':
            background_image = BASIC_DIR + 'media/bg_images/custom_white_image.jpg'
            save_background_image = BASIC_DIR + 'media/resize_images/test_custom_white_image_{}.jpg'.format(str(uuid.uuid4()).replace('-', '_'))
        else:
            background_image = BASIC_DIR + 'media/bg_images/bg-black.jpg'
            save_background_image = BASIC_DIR + 'media/resize_images/test_custom_bg-black_{}.jpg'.format(str(uuid.uuid4()).replace('-', '_'))
        image = cv2.imread(save_resize_image)
        image_width, image_height, dimension = image.shape

        white_image = cv2.imread(background_image, cv2.IMREAD_UNCHANGED)
        dim = (image_height, image_width)
        resized = cv2.resize(white_image, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(save_background_image, resized)
        combine_image(save_background_image, save_resize_image, save_resize_image)

    return save_resize_image_url


def combine_image(source_image, destination_image, file_name):
    im1 = Image.open(source_image)
    im2 = Image.open(destination_image).convert("RGBA")
    im1.paste(im2, (0, 0), im2)
    im1.save(file_name, quality=100)


def jpg_png_to_gif(data, save_user_image_path, white_image):
    save_resize_image_url, save_resize_image = get_file_name(data)
    images = [imageio.imread(save_user_image_path), imageio.imread(white_image)]
    imageio.mimsave(save_resize_image, images)
    return save_resize_image_url


def resize_gif(data, save_user_image_path):
    save_resize_image_url, save_resize_image = get_file_name(data)

    with Img(fp=save_user_image_path) as im:
        im.thumbnail(size=get_units(data))
        im.save(fp=save_resize_image)

    return save_resize_image_url
