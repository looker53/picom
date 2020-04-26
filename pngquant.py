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