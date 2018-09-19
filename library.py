class Human:
    def __init__(self, first_name, last_name, patronymic='', date_birth=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.date_birth = date_birth
        self.gender = gender

    def __str__(self):
        if self.patronymic:
            return f'человек:{self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f'человек:{self.last_name} {self.first_name[0]}'

    @classmethod
    def import_from_file(cls, file_name):
        items_source = open(file_name, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for item_dict in items_source_as_dict:
            _item = cls(**item_dict)
            items.append(_item)

        return items


class Student(Human):
    def __init__(self, first_name, last_name, date_birth, group, *args, **kwargs):
        super().__init__(first_name, last_name, *args, **kwargs)
        self.date_birth = date_birth
        self.group = group

    def set_group(self, group):
        self.group = group

    def __str__(self):
        if self.patronymic:
            return f'студент:{self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f'студент:{self.last_name} {self.first_name[0]}.'


class Group:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f'группа: {self.name} ({self.specialty.split()[-1]})'

    def add_students(self, students):
        for student in students:
            student.set_group(self)


class Librarian(Human):
    def __init__(self, first_name, last_name, patronymic, list_readers, books, *args, **kwargs):
        super().__init__(first_name, last_name, patronymic, *args, **kwargs)
        self.list_readers = list_readers
        self.books = books

    def __str__(self):
        if self.patronymic:
            return f'библиотекарь({self.list_readers}): {self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f'библиотекарь({self.list_readers}): {self.last_name} {self.first_name[0]}.{self.books[0]}.'


class Teacher(Human):
    def __init__(self, first_name, last_name, education, experience, *args, **kwargs):
        super().__init__(first_name, last_name, *args, **kwargs)
        self.education = education
        self.experience = experience

    @property
    def __str__(self):
        if self.patronymic:
            return f' учитель({self.education}): {self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f' учитель({self.education}): {self.last_name} {self.first_name[0]}.'

    @property
    def __str__(self):
        if self.patronymic:
            return f' студент({self.education}): {self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'
        else:
            return f' студент({self.education}): {self.last_name} {self.first_name[0]}.'
