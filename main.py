import bbcode
import re
from global_parser import GlobalRegistr
from level_one import OneLevel
text = """

Занятия будут проходить на базе бильярдного клуба «Меткий». Тренерский состав школы бильярда:
-- мастер спорта, главный тренер Федерации бильярдного спорта Иркутской области Владимир Шафиров;
-- кандидат в мастера спорта Глеб Луценко.

Расписание занятий: понедельник, среда, пятница в 10:00 и 15:00; вторник и четверг -- время будет зависеть от количества учеников.
[intro]Совсем скоро начнутся школьные будни не только для детей, но и для родителей. Утром -- школа, вечером -- английский или плавание. Шахматы или единоборства. А вы уже решили, чем займете ребенка после школы? Читайте обзор IRK.ru.[/intro]

Первое занятие состоится 13 сентября. Предварительное родительское собрание пройдет 7 сентября в 19:00.

Также открыт набор в школу бильярда для взрослых, занятия будут проходить в вечернее время три раза в неделю.
[intro]Совсем скоро начнутся школьные будни не только для детей, но и для родителей. Утром -- школа, вечером -- английский или плавание. Шахматы или единоборства. А вы уже решили, чем займете ребенка после школы? Читайте обзор IRK.ru.[/intro]
[video http://www.youtube.com/watch?v=xVXL2Kd5_tM]

[video http://vk.com/video194524705_164599841]

[video http://vimeo.com/17687260]

[video http://smotri.com/video/view/?id=v25948547cd9]
"""

def clear_line(text):
    regex_zero = r"\n^(\s)*$" ## clear пустые строчки
    regex_fix = r'[-]+\n[-]+' # clear ---\n---
    t = re.sub(regex_zero, "", text, 0, re.MULTILINE)
    t = re.sub(regex_fix, "", t, 0, re.MULTILINE)
    als = t.split('\n')
    if len(als)<2:
        return ""
    elif als[0] != '':
        return "\n".join(als[1:-1])
    elif als[0] == '':
        return "\n".join(als[2:-1])


def convert_to_pagraph(text):
    def __start(contex):
        regex = r"\]\n[-]+"
        subst = "]\n[paragraph]"
        result = re.sub(regex, subst, contex, 0, re.MULTILINE)
        return result

    def __stop(contex):
        regex = r"[-]+\n\["
        subst = "[/paragraph]\n["
        result = re.sub(regex, subst, contex, 0, re.MULTILINE)
        return result
    text = __stop(__start(text))
    return text


if __name__ == '__main__':
    gr= GlobalRegistr()

    parser = OneLevel(escape_html=False, newline="\n", install_defaults=False)
    parser.install_default_formatters() # loads b ,i ,other

    ## standolone tags
    parser.add_formatter('vladiff', gr.vladiff, standalone=True) #  +
    parser.add_formatter('diff', gr.diff, standalone=True) # +

    parser.add_formatter('image', gr.image, standalone=True) # +
    parser.add_formatter('images', gr.images, standalone=True) # +

    parser.add_formatter('card', gr.ember,standalone=True) # +
    parser.add_formatter('video', gr.ember,standalone=True) # +
    parser.add_formatter('ticket', gr.ticket, standalone=True) # +

    # tag requriments
    parser.add_formatter('audio', gr.file,standalone=True) # +

    ## install level one tags
    parser.add_formatter('spoiler', gr.spoiler)#+
    parser.add_formatter('intro', gr.intro) #+

    parser.add_formatter('ref', gr.ref)#+?
    parser.add_formatter("url", gr.url, replace_links=False, replace_cosmetic=False)#+?

    parser.add_formatter('cards', gr.cards)#?-
    parser.add_formatter('paragraph', gr.paragraph)#+?

    # trach
    parser.add_simple_formatter('file', '', standalone=True)

    t_clear = clear_line(parser.format(text))
    f = len(re.findall(r'\[count\s(\d+)\]',t_clear))

    if re.findall(r'\[count\s(\d+)\]',t_clear):
        t_text_wraper = convert_to_pagraph(t_clear)
        t_text_wraper = '[paragraph]' + t_text_wraper + '[/paragraph]'
        t = parser.format(t_text_wraper)
        print(gr.generate(t))
    else:
        """ случай когда нет ббкодов"""
        t_clear = '[paragraph]' + t_clear + '[/paragraph]'
        t = parser.format(t_clear)
        print(gr.generate(t))