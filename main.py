import bbcode
import re
from global_parser import GlobalRegistr
from level_one import OneLevel
text = """
[intro]Совсем скоро начнутся школьные будни не только для детей, но и для родителей. Утром -- школа, вечером -- английский или плавание. Шахматы или единоборства. А вы уже решили, чем займете ребенка после школы? Читайте обзор IRK.ru.[/intro]

[h2]Вариант №1. Английский язык в школе ABC[/h2]

Школа ABC[sup]1[/sup] имеет 29-летний опыт работы обучения иностранным языкам. За это время методистами школы была разработана многоуровневая программа обучения, которая позволяет организовать занятия максимально эффективно в интересной игровой форме.

[list]
[*]Для детей в возрасте от 5 до 7 лет -- уникальная программа Letterland[sup]2[/sup] по обучению чтению и письму. Эта методика разработана известным британским педагогом Лин Вендон. Секрет всемирного успеха заключается в методе пиктокодирования, когда каждой букве присваивается яркий образ героя волшебной страны букв. Это делает обучение захватывающим и интересным! Яркие и красочные карточки, игры, видео и песни позволяют детям без труда научиться читать и писать на английском языке.
[/list]

[images 15143804,15143803]

[list]
[*]Для школьников 1-3 классов – двухуровневая программа ABC Smart[sup]3[/sup]. Первый уровень включает самый прогрессивный курс по обучению чтению Smart Start[sup]4[/sup]. Это авторская разработка школы «Эй-Би-Си», благодаря которой ребенок научится читать за 35 занятий. Второй уровень, основанный на программе Smart Junior[sup]5[/sup], включает разнообразные лексические темы, аудирование и письменные упражнения при изучении грамматики. Активные игры, грамматические сказки, видео с героями любимых мультфильмов не оставят равнодушными ни одного ребенка.

[*]Для школьников 4-11 классов -- программа, базирующаяся на современных учебных материалах британских и американских издательств. Понятные грамматические схемы, уникальная система запоминания слов и развитие разговорной речи через дискуссии, ток-шоу и ролевые игры гарантирует 100% результат обучения английскому языку. 
[/list]

[images 15143801,15143802]

[list]
[*]Для старшеклассников -- курс по подготовке к сдаче государственных экзаменов ОГЭ и ЕГЭ. Занятия включают: подготовку к устной части; построение модели монолога согласно регламенту ЕГЭ и  ОГЭ; работа над фонетической выразительностью и грамотностью устной речи; интенсивное формирование активного словарного запаса; системное повторение всех необходимых правил по блокам;  решение демоверсий и тестов ЕГЭ и  ОГЭ по структуре экзамена, а также обучение написанию эссе по структуре и личного письма в соответствие с нормами ФИПИ.
[/list]

[images 15143805,15143806]

Школа ABC -- школа, которая даёт прочные знания!

[i]Школа ABC
Адреса и телефоны: 
улица Марата 54, [b](3952) 436-636[/b]
Омулевского 20/2, [b](3952) 436-686[/b]
проспект Жукова, 5/1, [b](3952) 431-831[/b]
улица Летописца Нита Романова 3, [b](3952) 436-854[/b]
Депутатская 84/1, [b](3952) 755-515[/b]

Телефон: [b](3952) 201-631[/b]

Страница во "Вконтакте" [url https://vk.com/abcirk]@abcirk[/url], "Инстаграм" [url https://www.instagram.com/abcirk/]@abcirk[/url]
Сайт: [url https://www.abc-irk.ru]abc-irk.ru[/url]
[/i]

[spoiler small Подробно]
[sup]1[/sup]эй-би-си
[sup]2[/sup]леттерлэнд
[sup]3[/sup]эй-би-си смарт
[sup]4[/sup]смарт старт
[sup]5[/sup] смарт джуниор
6+
[/spoiler]

[h2]Вариант №2. Курсы французского языка в "Альянс Франсез -- Иркутск"[/h2]

Центр французского языка и культуры «Альянс Франсез -- Иркутск» приглашает школьников и взрослых на курсы французского языка. Здесь можно начать изучение «с нуля» или пройти курс, который станет дополнением к урокам в школе и позволит подготовиться к ЕГЭ.

Программа включает в себя все основные аспекты изучения языка: фонетику, грамматику, говорение, аудирование, письмо, и дает надежную базу для подготовки к международным экзаменам, которые можно сдать по окончании курса. Занятия ведут квалифицированные педагоги, прошедшие обучение и стажировки во Франции, используются современные учебники французских издательств. Также есть возможность практиковать французский с носителями языка на тематических мероприятиях в дни школьных каникул и в разговорных клубах как онлайн, так и вживую.

[images 15143796,15143797,15143798,15143799]

[i]"Альянс Франсез -- Иркутск"
Адрес: Иркутск, Горького, 25, офис 104.
Телефон: [b]500-617[/b]

Сайт: [url https://afrus.ru/irkoutsk/]afrus.ru/irkoutsk[/url]
Страница во "Вконтакте" [url https://vk.com/afirkoutsk]@afirkoutsk[/url], "Фейсбуке" [url https://www.facebook.com/afirkoutsk]@afirkoutsk[/url], "Инстаграме" [url https://www.instagram.com/afirkoutsk/]@afirkoutsk[/url]
[/i]

[h2]Вариант №3. Учеба в центре дополнительного профессионального образования[/h2]

Учебный центр «Эталон» — крупнейший учебный центр дополнительного профессионального образования в Восточной Сибири. Высокий уровень преподавания, харизматичные педагоги,  оборудованные компьютерные классы, широкий ассортимент творческих направлений, курсы для взрослых, дополнительное образование для детей, полностью лицензированное программное обеспечение — все это делает нас известным и востребованным учебным центром.

Лицензированный учебный центр «Эталон» имеет разрешения на обучение по самым востребованным специальностям:

Мы являемся сертифицированным центром обучения 1С. Учеников обеспечат новейшими учебными пособиями фирмы 1С, по окончании получат сертификаты, дипломы и удостоверения установленного образца.

Также учебный центр «Эталон» -- официальный представитель компании Grafisoft*: можно пройти курсы Archicad** и получить сертификат международного образца.

[images 15143824,15143820,15143821,15143822]

[i]Лицензированный учебный центр «ЭТАЛОН»

Адрес: Иркутск улица Полины Осипенко, 13
Телефон: [b]72-72-80[/b]
Viber/WhatsApp: [b]8 901 663-33-99[/b]
Сайт: [url https://etalonkurs.ru]etalonkurs.ru[/url]
E-mail: [email etalonkurs.ru@mail.ru]etalonkurs.ru@mail.ru[/email][/i]

[spoiler small Подробно]
*графисофт
**архикад
[/spoiler]

[h2]Вариант №4. Набор детей и взрослых в школу бильярда[/h2]

Отделение бильярдного спорта при областной спортивной школе олимпийского резерва «Спарта» объявляет набор детей от 7 лет в школу бильярда.

"Отделение бильярдного спорта открыто в 2018 году и уже наши воспитанники показывают неплохие результаты на первенствах и чемпионатах Сибирского федерального округа", -- отметил вице-президент Федерации бильярдного спорта Иркутской области Владимир Верешня.

[images 15143817,15143811,15143812]

Занятия будут проходить на базе бильярдного клуба «Меткий». Тренерский состав школы бильярда:
-- мастер спорта, главный тренер Федерации бильярдного спорта Иркутской области Владимир Шафиров;
-- кандидат в мастера спорта Глеб Луценко.

Расписание занятий: понедельник, среда, пятница в 10:00 и 15:00; вторник и четверг -- время будет зависеть от количества учеников.

Первое занятие состоится 13 сентября. Предварительное родительское собрание пройдет 7 сентября в 19:00.

Также открыт набор в школу бильярда для взрослых, занятия будут проходить в вечернее время три раза в неделю.

[images 15143814,15143815]

[i]Школа бильярда

Телефоны: [b]95-15-0, 40-40-74[/b]
Сайт [url https://metkii.com]www.metkii.com[/url]
Страница в "Инстаграме" [url https://www.instagram.com/metkii_club/]@metkii_club/[/url]
[/i]

12+

[h2]Вариант №5. Уроки в клубе каратэ ИГУ[/h2]

Спортивный клуб каратэ Иркутского государственного университета объявляет о наборе детей и взрослых на новый спортивный сезон 2021-2022 года. Вид спорта: олимпийское каратэ WKF (World Karate Federation*). Стиль: каратэ шотокан (сетокан).

Желающих приглашают в:
[list]
[*]Детские группы от 5 лет, 
[*]Студенческие и взрослые группы от 16 лет, 
[*]Специальная адаптивная группа для людей с ограниченными возможностями здоровья. 
[/list]

[images 15143800,15143810]

Каратэ для детей -- это гарантия всестороннего физического и психологического развития вашего ребенка. Каратэ, как вид спорта, воспитывает в ребенке дисциплину, умение преодолевать себя. Осваивая разнообразную технику каратэ, дети учатся бить и держать удар, учатся побеждать и достойно принимать поражения не только на татами, но и в жизни. 

Каратэ, как восточное боевое искусство, имеет четкую систему жизненных ценностей, которую мы прививаем ребенку. Философия каратэ учит уважению, искренности и открытости, преодолевать трудности и добиваться поставленных целей, быть сдержанным, воспитывать самообладание и смирять гордыню.

[video https://youtu.be/ZfAFpsUbEkI]

Для взрослых – это хорошая возможность «перезагрузиться» после насыщенного рабочего дня. Занятия рекомендованы как мужчинам, так и женщинам -- каждый найдет для себя что-то свое.

Каратэ для людей с ограниченными возможностями здоровья --бесконтактный, безопасный и захватывающий вид спорта, развивающий человека умственно, эмоционально и физически. Этот вид спорта доступен практически для всех нозологических групп и любого возраста.
Если вы и ваш ребенок еще не в нашей команде,  приглашаем именно вас.

[images 15143808,15143807,15143809]

[i]Клуб каратэ ИГУ

Телефон: [b]8 924 700-94-93[/b]
Страница в "Инстаграме": [url https://www.instagram.com/karate_isu/?hl=ru]@karate_isu[/url] 
[/i]

[small]
*Всемирная федерация каратэ
12+
[/small]

[h2]Вариант №6. Обучение IT и дизайну в "Компьютерной академии ШАГ"[/h2]

Крупный международный учебный центр IT*-образования "Компьютерная академия ШАГ" предлагает обучение детям и взрослым. У академии -- более 165 филиалов в 22 странах, где обучение идет по единой программе. При желании студент может начать обучение в Иркутске, а закончить, например, в Сиэтле.

[image 15143826]

Начала Академия свою работу в 1999 году с профессиональной подготовки программистов, компьютерных дизайнеров, специалистов в области сетей и информационной безопасности. В программу обучения входят авторизованные курсы от ведущих мировых компаний — Microsoft, Cisco, Autodesk, что позволяет получить международные сертификаты еще в процессе обучения. Студенты «ШАГа» побеждают на международных IT-конкурсах, выпускники работают в крупнейших мировых компаниях — Microsoft, Google, HP, Ebay, Amazon и многих других.

[video https://www.youtube.com/watch?v=HVXy6IdjeAU]

Приглашаем 11 сентября на день открытых дверей. Детям проведут бесплатный мастер-класс — «Создание 3D**-героя Майнкрафт», а для родителей пройдёт специальная презентация об обучении для детей в сфере IT. На мероприятие можно записаться через [url https://irk.itstep.org/events/master-class-for-children-8-12-years-old-3d-modeling-of-the-character-of-the-game-minecraft?utm_source=irk.ru&utm_medium=article&utm_campaign=dod_09]форму на сайте[/url].

[image 15143827]

[i][url https://irk.itstep.org/events/master-class-for-children-8-12-years-old-3d-modeling-of-the-character-of-the-game-minecraft?utm_source=irk.ru&utm_medium=article&utm_campaign=dod_09]Компьютерная Академия «ШАГ»[/url]
Адрес: Советская, 58 к 3, 1-й этаж
Телефон: [b]48-20-12[/b]
Сайт: [url https://irk.itstep.org/events/master-class-for-children-8-12-years-old-3d-modeling-of-the-character-of-the-game-minecraft?utm_source=irk.ru&utm_medium=article&utm_campaign=dod_09] [image 15143826]
irk.itstep.org[/url]
Задать вопросы можно через WhatsApp: [url https://api.whatsapp.com/send?phone=79642624944]+7 964-262-49-44[/url].[/i]

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
    t_text_wraper = convert_to_pagraph(t_clear)
    t = parser.format(t_text_wraper)
    print(gr.generate(t))
