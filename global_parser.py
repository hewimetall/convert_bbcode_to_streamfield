import json
import logging
import re
import uuid

class BaseGlobalRegistr:
    """
        Регистр данных
        хранить структуру

            - dict
                -- key = индификатор обьекта
                -- value = json данные для вставки

    """
    _list_regist = {}
    _q = []
    count = 0

    def get_count(self, id: int):
        return self._list_regist[id]

    def __set_count(self, obj, name: str) -> int:
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
        id = self.__set_count(obj, name)
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

    def paragraph(self, tag_name: str, value: str, options: dict, parent, context):
        name = tag_name
        id = self.__set_count(value, name)
        return f"\n[count {id}]\n"


class BaseMixTreeJson(BaseGlobalRegistr):
    """
        Отвечает за создания из синтаксической структуры  представления для wagtail
    """
    __tree_index = [

    ]

    def root_has_childs(self, id: int, count_list: list):
        pass

    def root_not_has_childs(self, id: int):
        pass

    def gen_root_node(self, count: id, child=None):
        if child:
            name, value = self.root_has_childs(count, child)
        else:
            name, value = self.root_not_has_childs(count)

        if isinstance(value,dict):
            self.__tree_index.append(
                {
                    "type": name,
                    "value": value,
                    "id":str(uuid.uuid4())
                }
            )
        elif isinstance(value,list):
            """ Fix from gallary """
            self.__tree_index.append(
                {
                    "type": name,
                    "value": value,
                    "id": str(uuid.uuid4())
                }
            )
        elif isinstance(value,set):
            self.__tree_index.append(
            {
            "type": name,
            "value": value.pop(),
            "id": str(uuid.uuid4())
            }
            )
        elif isinstance(value,str):
            self.__tree_index.append(
            {
            "type": name,
            "value": value,
            "id": str(uuid.uuid4())
            }
            )
        else:
            self.__tree_index.append(
                {
                    "type": name,
                    "value": value[0],
                    "id": str(uuid.uuid4())
                }
            )

    def gen_multi_stret(self, counts: list):
        counts = [int(i) for i in counts]  # Преобразуем в инт
        counts.reverse()  # Для того чтобы получить правельный порядок обьектов
        root_id = counts[0]
        child_counts = counts[1:]  # удаляем родительсткий обьект
        # !TODO: добавить реализацию для вложений
        self.gen_root_node(
            root_id,
            child_counts
        )

    def gen_one_stret(self, count: int):
        self.gen_root_node(count)

    def generate(self, text: str):
        text_clear = re.sub(r'$\n', '', text, 0, re.MULTILINE)
        regex = r"\[count (?P<ids>[^\]]+)"
        result = re.findall(regex, text_clear, re.MULTILINE)
        ### Генерируем верхнее ноды
        for row in result:
            counts = row.split(',')
            if len(counts) > 1:
                self.gen_multi_stret(counts)
            else:
                self.gen_one_stret(int(counts[0]))
        return json.dumps(self._BaseMixTreeJson__tree_index,ensure_ascii=False)


class MixTreeJson(BaseMixTreeJson):
    ''' '''

    def root_has_childs(self, id: int, count_list: list):
        name, value = self.get_count(id)
        if name == self.get_count(id):
            pass
        return name, value

    def root_not_has_childs(self, id: int):
        return self.get_count(id)


class GlobalRegistr(MixTreeJson):
    """ Отвичает за создания синтаксической структуры
        Преобразует текст в синтаксическое дерево для создания json структуры
    """


    def _check_image(self, image)->int:
        return int(image)

    def _check_file(self, id_file)->int:
        return int(id_file)

    def _rich_text(self,value)->str:
        return value

    def _none_block(self,value:str,tag:str):
        """ Вызывается когда не может произвести перевод """
        return "none_block", f"[{tag}]f{value}[/f{tag}]"
    def _replace(self, data, replacements):
        """
        Given a list of 2-tuples (find, repl) this function performs all
        replacements on the input and returns the result.
        """
        for find, repl in replacements:
            data = data.replace(find, repl)
        return data

    def _render_url(self, options):
            if len(options):
                href = list(options.keys())[0]
                REPLACE_ESCAPE = (
                    ("&", "&amp;"),
                    ("<", "&lt;"),
                    (">", "&gt;"),
                    ('"', "&quot;"),
                    ("'", "&#39;"),
                )
                # Option values are not escaped for HTML output.
                for find, repl in REPLACE_ESCAPE:
                    href = href.replace(find, repl)
            else:
                href = ''
            # Completely ignore javascript: and data: "links".
            if re.sub(r"[^a-z0-9+]", "", href.lower().split(":", 1)[0]) in ("javascript", "data", "vbscript"):
                return ""
            # Only add the missing http:// if it looks like it starts with a domain name.
            if "://" not in href:
                href = "http://" + href

            #'<a href="%s">%s</a>' % href , value
            return href


    def url (self, tag_name: str, value: str, options: dict, parent, context, is_root=None):
        href = self._render_url(options)
        regex = r"\[count\s(\d+)\]"
        swap_url = re.findall(regex, value, re.MULTILINE)
        if swap_url:
            for i in swap_url:
                child_name, child_value = self._list_regist[int(i)]
                if child_name == "image":
                    child_value['url'] = href
                else:
                    child_name, child_value = self._none_block(value, tag_name)
            return self.multi_reg(value, child_value, child_name)
        else:
            return f'<a href="{href}">{value}</a>'

    def spoiler(self, tag_name: str, value: str, options: dict, parent, context, is_root=None):
        text = ""
        is_small = False
        for i in options:
            if i == "small":
                is_small = True
            else:
                text += " " + i
        if is_root:
            d = {
                'is_small':is_small,
                'span_text':text,
                'none_block':text
            }
        else:
            d = {
                'is_small': is_small,
                'span_text': text,
                'paragraph': self._rich_text(value)
            }
        return self.multi_reg(value, d, "spoiler")

    def diff(self, tag_name: str, value: str, options: dict, parent, context):
        i1, i2 = -1, -1
        after = ''
        before = ''
        for i in options:
            if i == 'after':
                after = options[i]
            elif i == 'before':
                before = options[i]
            else:
                if len(i.split(",")) == 2:
                    i1, i2 = i.split(',')
                else:
                    if i1 < 0:
                        i1 = i
                    elif i2 < 0:
                        i2 = i
            old = self._check_image(i1)
            new = self._check_image(i2)

            return self.multi_reg('',{
                    "after": after,
                    "before":before,
                    "old":old,
                    "new":new
            } , "diff")

    def vladiff(self, *args, **kwargs):
        return self.diff(*args, **kwargs)

    def cards(self, tag_name: str, value: str, options: dict, parent, context):
        name, d = self._none_block(value, tag_name)
        return self.multi_reg(value, d, name)

    def intro(self, tag_name: str, value: str, options: dict, parent, context):
        return self.multi_reg('', {
            self._rich_text(value)
        }, 'intro')

    def image(self, tag_name: str, value: str, options: dict, parent, context):
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

        options = align
        try:
            stretch = options[3]
            options += "," + stretch
        except:
            pass

        image = self._check_image(pk)

        if link_3d:
            # !TODO 3d add logick if url
            name = 'tour'
            d = {
              "id_image": {
                "image": int(image),
              },
              "url": link_3d
            }
        else:
            name = 'image'
            d = {
            "image": int(image),
            "options": options,
        }

        return self.multi_reg('', d, name)

    def images(self, tag_name: str, value: str, options: dict, parent, context):
        if len(options) >= 1:
            id_list = ''.join(options)
            id_list = id_list.split(',')
        elif len(options) < 1:
            return '\n'
        images = []
        for i in id_list:
            image = {
                "type": "image",
                "value": {
                    "image": int(i),
                    "options": ""
                },
                "id": str(uuid.uuid4())
            }
            images.append(image)
        return self.multi_reg('',
            images
        , "gallery")

    def file(self, tag_name: str, value: str, options: dict, parent, context):
        """ВВ код [audio]
[{"type": "document", "value": {"docs": 2, "url": "test", "value": "setset"}, "id": "8fdd9233-44a0-4c0c-adf2-e7367d1fc214"}]
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
            file_id = self._check_file(src)
            d = {
                "docs": file_id,
            }

        # from irk.uploads.models import Upload
        # try:
        #     obj = Upload.objects.get(id=src)
        # except Upload.DoesNotExist:
        #     return ''
        # src = obj.file.url
        # title = value if value else obj.title
        elif not src.startswith(('http://', 'https://')):
            # относительный урл - от корня media
            # src = settings.MEDIA_URL + src
            d = {
                "url": src,
            }
        else:
            return ''
        d["value"] = value
        return self.multi_reg('',d, "document")


    def ticket(self, tag_name: str, value: str, options: dict, parent, context):
        """BB код [ticket]"""

        event: str = list(options)[0]
        if event.isdecimal():
            d = {
                "event_id": event,
            }
        elif event.startswith(('http://', 'https://', 'www')):
            url_split = event.split("/")
            event_id = url_split[-1] if url_split[-1].isdecimal() else url_split[-2]
            d = {
                "event_id": event_id,
                "url": event
            }
        else:
            return ''
        return self.multi_reg('', d, "ticket")

    def ref(self, tag_name: str, value: str, options: dict, parent, context):
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
          {
        """

        if not value:
            return ''
        args = (','.join([k for k in options.keys()])).split(',')

        if len(args) == 2:
            source = args[0]
            href = args[1]
        elif len(args) == 1:
            source = args[0]
            href = None
        else:
            source = None
            href = None
        d ={
            "source": source,
            "url": href,
            "value": value
        },
        return self.multi_reg('', d, 'ref')

    def ember(self, tag_name: str, value: str, options: dict, parent, context):
        href = list(options.keys())

        url = href[0]
        url_base = url +"="+ options[url]
        args_list = [url_base]
        for i in href[1:]:
            args_list.append( url + "=" + options[url] )
        if len(args_list)>1:
            url_all = "&".join(args_list)
        elif options[url] != "":
            url_all = url
        else:
            url_all = url_base
        return self.multi_reg('', str(url_all), "embed")

    def card(self, tag_name: str, value: str, options: dict, parent, context):
        href = list(options.keys())
        url = href[0]
        url_base = url +"="+ options[url]
        args_list = [url_base]
        for i in href[1:]:
            args_list.append( url + "=" + options[url] )
        url_all = "&".join(args_list)
        return self.multi_reg('', f"<ticket>{href}</ticket>", tag_name)
