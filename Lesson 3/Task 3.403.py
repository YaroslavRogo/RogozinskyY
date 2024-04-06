from CommonUtils import CommonUtils

class SlugConverter:
    def __init__(self):
        self._file_name = input('Введите название файла: ')
        self._slug_list = []
        self.run()

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def slug_list(self):
        return self._slug_list

    def run(self):
        while True:
            s = input('Введите ФИО известных людей. Для завершения программы введите пустую строку: ')
            if s == '':
                break
            slug = CommonUtils.translit_to_eng(s)
            self._slug_list.append(slug)
            print('Slug: ' + slug)

        self.save_to_file()

    def save_to_file(self):
        with open(self._file_name, 'w') as file:
            for slug in self._slug_list:
                file.write(slug + '\n')

        print('Данные были сохранены в файл:', self._file_name)


slug_converter = SlugConverter()