

def translit_to_eng(s):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya', ' ': '-'
    }

    s = s.lower()
    slug = ''
    for char in s:
        if char in translit_dict:
            slug += translit_dict[char]
    return slug


while True:
    s = input('Введите ФИО известных людей. Для завершения программы введите пустую строку: ')
    if s == '':
        break
    slug = translit_to_eng(s)
    print('Slug: ' + slug)