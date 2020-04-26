from PIL import Image


def compress_name(fp):
    """通过之前的"""
    pass

def compress_jpg(fp, output, quality=None):
    """
    通过 quality 参数压缩.
    quality 参数主要用来压缩 JPEG 格式。不能用来处理 png.
    :param fp: 处理图片，名称或者是 file obj
    :param output: 保存的图片名称
    :param quality: 压缩质量
    :return:
    """
    im: Image.Image = Image.open(fp)
    im.save(output, quality=quality)


def compress_png(fp, output):
    """直接使用 optimize 的效果不好。需要模式转化"""
    im: Image.Image = Image.open(fp)
    im.save(output, optimize=True)

def quantize(fp, output):
    im: Image.Image = Image.open(fp)
    im.show()
    new_im = im.quantize()
    new_im.show()







