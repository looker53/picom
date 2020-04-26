## 开发一款图片压缩工具（二）：使用 pngquant 实现图片压缩 

上一篇我尝试使用了 pillow 库对 png 图片进行了压缩，效果不好。这次我换用 pngquant 来压缩。
pngquant是用于PNG图像有损压缩的命令行实用程序和库。压缩程序会显著减小文件大小（通常高达70%），并保持完全的alpha透明度。
通过使用alpha通道将图像转换为更高效的8位PNG格式（通常比24/32位PNG文件小60-80%）。

pngquant 使用的算法主要是中值切割量化算法的改进版和 K-means 颜色校正。得到的图片颜色差异肉眼几乎无法察觉。

这是 pngquant 优化后的图片：

这是 pillow 同样采用中值切割和 k-means 得到的优化效果：




### pngquant 压缩库使用

pngquant 提供了源码、命令行和 GUI 等多种形式。
GUI 的工具目前来说还比较难用，并没有命令行方便，而源码形式可以通过 ctype 使用 python语言去调用 c 源码。
但是目前对这方面还不怎么了解，可以后面再去使用 so 动态库等放手。

所以，先用命令行形式进行 PNG 压缩。

1，下载[windows安装包](https://pngquant.org/pngquant-windows.zip) 或者 mac 和 linux 版本的安装包。
2，命令行输入 `pngquant` 就可以使用了；
3，为了使用方便，可以配置环境变量，后面如果和 picom 集成在了一起再去掉。
![pngquant-fs8.png](https://i.loli.net/2020/04/24/JGkdOQ6VU2Fjbfa.png)


#### 快速使用 pngquant
```
pngquant 图片名称.png
```

对于一些可选参数的说明：

1，--skip-if-larger
pngquant 有时候压缩的文件会比源文件大。这个选项会判断，如果大就取消执行。**强烈建议加上**


2，--quality 0-100
图片质量。对于颜色没有特别要求的可以缩减到 10， 但是越小压缩率越低，通常不需要设置。

1，`--force`
强制执行，pngquant 会判断，如果有一个已经压缩的同名文件在当前文件夹，就不会执行。这个选项会覆盖原来的文件。




3，--output file
指定输入文件的名称。 可以指定为 jpg 格式，但是图片不会变得更小。

4，--speed 速度


#### 使用 subprocess 调用 pngquant 命令行 

对应的程序：
```python
import subprocess
subprocess.run('pngquant elephant.png')
```

如果想获取程序运行时屏幕上显示的内容，可以使用 check_output 方法，在这里不需要。


接下来使用 subprocess 封装对应的压缩函数：
```python
def pngquant_compress(fp, force=False, quality=None):
    """压缩函数.
    
    参数：
        fp: 文件名称
        force: 如果存在同名文件，是否覆盖
        quality: 压缩质量。 10-40， or 10
    """
    force_command = '-f' if force else ''
    
    quality_command = ''
    if quality and isinstance(quality, int):
        quality_command = f'--quality {quality}'
    if quality and isinstance(quality, tuple):
        quality_command = f'--quality {quality[0]}-{quality[1]}'
    
    command = f'pngquant {fp} --skip-if-larger {force_command} {quality_command}'
    subprocess.run(command)


if __name__ == "__main__":
    pngquant_compress('elephant.png', force=True, quality=20)
```


### 参考文章
[subprocess资料]()



## 开发一款图片压缩工具（三）：使用 click 实现命令行