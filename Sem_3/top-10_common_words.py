'''
В большой текстовой строке подсчитать количество встречаемых слов
и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''


text = ('Монти Пайтон считается революционным явлением в жанре абсурдистского юмора, '
        'сделавшего его одним из самых популярных направлений комедийного искусства. '
        'В Монти Пайтонах лежат истоки таких популярных явлений культуры, '
        'как комедийное шоу Фрая и Лори, мультсериал Южный парк и многих других. '
        'В своём восхищении Монти Пайтонами признались Маргарет Тетчер, Вячеслав Полунин. '
        'По одной из версий, термин спам (SPAM) вошёл в обиход благодаря знаменитому скетчу '
        'с одноимённым названием из телешоу «Летающий цирк Монти Пайтона». '
        'Смысл скетча сводится к тому, что в одном кафе все блюда в меню содержат «SPAM» '
        '(в реальности — торговая марка консервированного мяса), некоторые даже по нескольку раз. '
        'Когда главный герой скетча, пришедший в это кафе вместе с женой, просит принести ему '
        'блюдо без «SPAMа», официантка предлагает ему блюдо с «небольшим количеством SPAMа». '
        'Посетитель возмущается, а хор викингов, сидящих за соседними столиками, начинает петь '
        'хвалебную песню «SPAMу», после чего скетч погружается в хаос. В конце скетча жена героя '
        'восклицает: «I don’t like spam!» (Я не люблю «SPAM»!). В титрах к именам исполнителей '
        'также было добавлено слово «SPAM». В общей сложности это слово упоминается в скетче 108 раз. '
        'Язык программирования Python назван в честь «Монти Пайтона».')

text_without_chars = (text.replace(',', '')
                      .replace('.', '')
                      .replace(' -', '')
                      .replace('(', '')
                      .replace(')', '')
                      .replace('«', '')
                      .replace('»', '')
                      .replace('!', ''))
text_list = sorted(text_without_chars.lower().split())
words_dict = dict()
for word in text_list:
    words_dict[word] = text_list.count(word)

for key, value in sorted(words_dict.items(),key=lambda para: (-para[1],para[0]))[:10]:
    print(f'{key}: {value}')