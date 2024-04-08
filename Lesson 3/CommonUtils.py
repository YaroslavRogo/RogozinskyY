class CommonUtils:
    @staticmethod
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


"""
class SlugConverter:
    def __init__(self):
        self.file_name = input('Введите название файла: ')
        self.slug_list = []
        self.run()


    def run(self):
        while True:
            s = input('Введите ФИО известных людей. Для завершения программы введите пустую строку: ')
            if s == '':
                break
            slug = CommonUtils.translit_to_eng(s)
            self.slug_list.append(slug)
            print('Slug: ' + slug)

        self.save_to_file()

    def save_to_file(self):
        with open(self.file_name, 'w') as file:
            for slug in self.slug_list:
                file.write(slug + '\n')

        print('Данные были сохранены в файл:', self.file_name)


slug_converter = SlugConverter()
"""