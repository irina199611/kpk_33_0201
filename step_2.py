from library import Student

# students_source = [
# {
#     'first_name': 'Петр',
#     'last_name': 'Игнатьев',
#     'patronymic':'Ильич',
#     'date_birth':'10.09.1998',
#     'gender': 'M'
# },
# ]
# print(students_source[0])
#
# student_1 = Student(**students_source[0])
# print(student_1)
#
# student_2 = Student(first_name='Петр', last_name='Игнатьев', patronymic='Ильич', date_birth='10.09.1998', genger='M')

students_source = open('students.src', 'r', encoding='utf-8').readlines()
students_source = list(map(lambda x: x.replace('\n', '').split(', '), students_source))
# print(students_source)

students_schema = students_source.pop(0)
# print(students_schema)

students_source_as_dict = list(map(lambda x: dict(zip(students_schema, x)), students_source))
# [print(el) for el in students_source_as_dict]

students = []
for student_dict in students_source_as_dict:
    _student = Student(**student_dict)
    students.append(_student)

[print(el) for el in students]