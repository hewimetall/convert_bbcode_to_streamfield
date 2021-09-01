def diff_formatter(name, value, options, parent, context):
    """
    BB код [diff]. Используется для вывода слайдера до - после.

    Примеры использования:
        [diff 113322,445566]
        [diff 113322, 445566 before="2009" after="2015"]
    """

    # Вырезаем именнованные параметры

    before_label = params.get('before', '')
    after_label = params.get('after', '')

    # Идентификаторы через запятую с пробелом
    if len(options) > 1:
        options = [''.join(options)]
    elif len(options) < 1:
        return ''

    id_list = options[0].split(',')

    pictures = []
    for pk in id_list:
        try:
            gallery_picture = GalleryPicture.objects.select_related('picture').get(pk=pk)
            pictures.append(gallery_picture.picture)
        except GalleryPicture.DoesNotExist:
            logger.warning('Does not exist object with pk {}'.format(pk))
            continue

    if len(pictures) < 2:
        return ''

    result = render_to_string('bb_codes/diff_slider.html', {
        'picture_1': pictures[0],
        'picture_2': pictures[1],
        'before_label': before_label,
        'after_label': after_label,
    })
    # Удаляем символы переноса строки, т.к. при выводе типограф применяет фильтр linebreaks
    return result.replace('\n', '')


def audio_formatter(name, value, options, parent, context):
    """ВВ код [audio]

    Используется для вставки плеера аудиофайла. Например:
        [audio 1489]
        [audio img/site/uploads/2018/12/75b2b0ad4b7ee0a470240c8f8b091773e142f4a5.mp3]
        [audio http://example.com/song.mp3]Какой-то дополнительный тайтл[/audio]
    """
    src = options[0]
    title = value or ''

    if src.isdecimal():
        from irk.uploads.models import Upload
        try:
            obj = Upload.objects.get(id=src)
        except Upload.DoesNotExist:
            return ''
        src = obj.file.url
        title = value if value else obj.title

    elif not src.startswith(('http://', 'https://')):
        # относительный урл - от корня media
        src = settings.MEDIA_URL + src

    return render_to_string('bb_codes/audio.html', {
        'id': random.randint(1, 999999),
        'src': src,
        'title': title,
    })


def file_formatter(name, value, options, parent, context):
    """BB код [file]

    Есть два варианта использования кода:
        - передается ссылка
        - передается идентификатор объекта модели :class:`irk.pages.models.File`
    """

    href = options[0]

    try:
        align = ' align={0}'.format(options[1])
    except IndexError:
        align = ''

    size = ''

    if href.isdigit():
        from irk.pages.models import File
        try:
            obj = File.objects.get(id=href)
        except File.DoesNotExist:
            # TODO: logger.warning()
            return ''

        href = obj.file.url
        try:
            image = Image.open(obj.file.path)
        except IOError:
            return ''
        size = ' style="width:{0}px;height:{1}px;"'.format(*image.size)

    value = value or ''

    name, ext = os.path.splitext(href)
    if ext in _image_extensions:
        return u'<img src="{href}" alt="{title}" title="{title}"{align}{size}>'.format(href=href, title=value,
                                                                                       align=align, size=size)
    return u'<a href="{href}">{title}</a>'.format(href=href, title=value)
