import logging

import click

from . import pngquant


class QualityInteger(click.ParamType):
    name = "QualityInteger"

    def convert(self, value, param, ctx):
        if value.isdigit():
            return int(value)
        try:
            min_v, max_v = value.split('-')
            int(min_v), int(max_v)
            return value
        except ValueError:
            self.fail('参数不符合类似 20-30 或者 30 的规范')


@click.command()
@click.argument('fp')
@click.option('--force', '-f', '--violent', is_flag=True, help='强制执行')
@click.option('--quality', '-q', type=QualityInteger(), help='压缩质量')
def cli(fp, force, quality):
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(f"正在优化:{fp}...")
    pngquant.pngquant_compress(fp, force, quality)
    logging.info(f"优化完成:{fp}!请打开文件夹查看 *-fs8")


