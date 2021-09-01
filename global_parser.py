import  re


class BaseGlobalRegistr:
    _list_regist = {}
    _q = []
    count = 0

    def __gen_count(self, obj, name) -> int:
        self._list_regist[self.count] = (name, obj)
        self.count += 1
        return self.count - 1

    def __gen_index(self, count: list):
        count_list = ",".join([str(i) for i in count if int(i) in self._list_regist])
        return f"\n{'-' * 6}\n[count {count_list}]\n{'-' * 6}\n"

    def __search_parrent(self, value) -> list:
        m: list[tuple] = re.findall(R"count(?P<v>([^\]])+)", value)
        if len(m):
            l_v = [i[1] for i in m]
            return l_v
        else:
            return None

    def _register(self, obj, name, childs: list = None):
        id = self.__gen_count(obj, name)
        if childs:
            childs.append(id)
            return self.__gen_index(childs)
        return self.__gen_index([id, ])

    def multi_reg(self, value: str, obj, name):
        childs = self.__search_parrent(value)
        if childs:
            return self._register(obj, name, childs)
        else:
            return self._register(obj, name)


class GlobalRegistr(BaseGlobalRegistr):

    def spoiler(self, tag_name:str, value:str, options:dict, parent, context):
        text = ""
        for i in options:
            if i == "small":
                pass
            else:
                text += " "+i
        return self.multi_reg(value,f"<spoiler>{text}</spoiler>","spoiler")

    def diff(self, tag_name:str, value:str, options:dict, parent, context):
        i1,i2 = -1,-1
        for i in options:
            if i == 'before':
                pass
            elif i == 'before':
                pass
            else:
                if len(i.split(",")) ==2: i1,i2 = i.split(',')
                else:
                    if i1 < 0:
                        i1 = i
                    elif i2 < 0:
                        i2 = i

            return self.multi_reg('',f"<diff>{i1}--{i2}</diff>","diff")

    def vladiff(self,*args, **kwargs):
        return self.diff(*args, **kwargs)

    def q(self,*args, **kwargs):
        return self.spoiler(*args, **kwargs)

    def cards(self,*args, **kwargs):
        return self.spoiler(*args, **kwargs)

    def intro(self,*args, **kwargs):
        return self.spoiler(*args, **kwargs)

    def image(self, tag_name:str, value:str, options:dict, parent, context):
        """BB код [image]

        Примеры использования::
            [image 12345], где 12345 идентификатор объекта :class:`irk.gallery.models.GalleryPicture`
            [image 12345 center] - изображение с выравниванием по центру
            [image 12345 right] - изображение с выравниванием по правому краю
            [image 12345 center 625x1000 stretch] - изображение с выравниванием по центру
                                                    с кастомным масшатабированием (625х1000) и растягиванием блюром
            [image 12345 3d_tour=http://irkutskoil.ml/] - изображение с сылкой на 3D тур
        """

        # Получение url 3D тура
        link_3d = None
        if "3d_tour" in options:
            link_3d = options['3d_tour']

        pk = list(options.keys())[0]
        try:
            align = options[1]
            if align not in ('left', 'center', 'right'):
                raise ValueError()
        except:
            align = 'center'

        return self.multi_reg('', f"<diff>{align}--{link_3d}</diff>", "diff")

    def images(self, tag_name:str, value:str, options:dict, parent, context):
        if len(options) >= 1:
            id_list = ''.join(options)
            id_list = id_list.split(',')
        elif len(options) < 1:
            return '\n'
        return self.multi_reg('', "<diff></diff>", "diff")


    def audio(self, tag_name:str, value:str, options:dict, parent, context):
        """ВВ код [audio]

        Используется для вставки плеера аудиофайла. Например:
            [audio 1489]
            [audio img/site/uploads/2018/12/75b2b0ad4b7ee0a470240c8f8b091773e142f4a5.mp3]
            [audio http://example.com/song.mp3]Какой-то дополнительный тайтл[/audio]
        !TODO:
                - Не забыть запретить дитей
        """

        title = value or ''
        src = list(options.keys())[0]
        if src.isdecimal():
            pass
           # from irk.uploads.models import Upload
           # try:
           #     obj = Upload.objects.get(id=src)
           # except Upload.DoesNotExist:
           #     return ''
           # src = obj.file.url
           # title = value if value else obj.title
        elif not src.startswith(('http://', 'https://')):
            # относительный урл - от корня media
            #src = settings.MEDIA_URL + src
            pass
        return self.multi_reg(title, "<audio></audio>", "audio")


    def h(self, tag_name:str, value:str, options:dict, parent, context):
        return self.multi_reg('', f"<{tag_name}>{value}</{tag_name}>", tag_name)


    def ticket(self, tag_name:str, value:str, options:dict, parent, context):
        """BB код [ticket]"""

        event:str = list(options)[0]
        if event.isdecimal():
        #event = Event.objects.filter(pk=event_id).select_related('type').first()
            event_id = event
        elif event.startswith(('http://', 'https://','www')):
            url_split = event.split("/")
            event_id = url_split[-1] if url_split[-1].isdecimal() else url_split[-2]
        else:
            return ''
        return self.multi_reg('',f"<ticket>{event_id}</ticket>",tag_name)


    def ref(self, tag_name:str, value:str, options:dict, parent, context):
        """
        BB-код [ref <source> <href>]<content>[/ref] для вставки сноски в текст
        Параметры:
            source - источник информации
            href - ссылка на источник
            content - содержание сноски

        Примеры использования:
            [ref]Джон Барлоу утверждает...[/ref]
            [ref IRK.RU]Джон Барлоу утверждает...[/ref]
            [ref IRK.RU http://irk.ru]Джон Барлоу утверждает...[/ref]
        """

        if not value:
            return ''
        args = (','.join([k for k in options.keys()])).split(',')


        if len(args) == 2:
            source = args[0]
            href = args[1]
        elif len(args) == 1 :
            source = args[0]
            href = None
        else:
            source = None
            href = None

        return self.multi_reg('',f"<ticket>{source}</ticket>",tag_name)


    def video(self, tag_name:str, value:str, options:dict, parent, context):
        href = list(options.keys())
        return self.multi_reg('',f"<ticket>{href}</ticket>",tag_name)

    def card(self, tag_name:str, value:str, options:dict, parent, context):
        href = list(options.keys())
        return self.multi_reg('',f"<ticket>{href}</ticket>",tag_name)
