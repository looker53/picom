import subprocess
from pathlib import Path
import requests


class PNGQuant:
    quant = Path(__file__).absolute().parent / 'ext/pngquant.exe'

    def compress_png_quant(self, file, *others):
        """
        通过 png quant 压缩
        :param files: 需要压缩的文件
            可以是： '.', 压缩当前目录下所有的 png 文件；
            也可以是：'demo.png', 'demo1.png'
        :return:
        """
        file_path = Path(file)
        if file_path.is_dir():
            cmd = [f.name for f in file_path.iterdir() if
                   f.suffix == '.png' and "fs8" not in f.name]
        else:
            files = list(others)
            files.insert(0, file)
            cmd = [Path(f).name for f in files if
                   Path(f).exists() and "fs8" not in Path(f).name]

        cmd.insert(0, self.quant)
        subprocess.run(cmd, shell=True)

        cmd.pop(0)
        return cmd

    def compress(self, file, *others, upload=True):
        """压缩函数，可以上传"""
        files = self.compress_png_quant(file, *others)
        if not upload:
            return files

        loader = Uploader()
        res = [loader.upload_sm(f) for f in files]
        loader.close()
        return res


class Uploader:
    def __init__(self):
        self.session = requests.Session()

    def upload_sm(self, file):

        api_addr = 'https://sm.ms/api/v2'
        upload_api = '/upload'
        url = api_addr + upload_api

        files = {
            "smfile": open(file, 'rb')
        }

        res = self.session.post(url, files=files)

        resp = res.json()
        code = resp.get('code')

        if code == 'image_repeated':
            url = resp.get('images')
            return (file, url)
        elif code == 'success':
            return (file, resp.get["data"]["url"])

    def close(self):
        self.session.close()


if __name__ == '__main__':
    PNGQuant().compress_png_quant('.')
