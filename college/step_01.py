from college import Student, Group, Teacher

# students = Student.import_from_file('students_33.src')
# [print(el) for el in students]

print('*' * 25)
students_23 = Student.import_from_file('students_23.src')
group_23 = Group('23', 'Прикладная информатика 09.02.05')
group_23.add_students(students_23)
[print(el, el.group) for el in students_23]

print('*' * 25)
students_33 = Student.import_from_file('students_33.src')
group_33 = Group('33', 'Прикладная информатика 09.02.05')
group_33.add_students(students_33)
[print(el, el.group) for el in students_33]

print('*' * 25)
students_43 = Student.import_from_file('students_43.src')
group_43 = Group('43', 'Дошкольное образование 44.02.01')
group_43.add_students(students_43)
[print(el, el.group) for el in students_43]

print('*' * 25)
teachers = Teacher.import_from_file('teachers.src')
[print(el) for el in teachers]
