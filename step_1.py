from library import Student, Librarian, Teacher, Group

# students = Student.import_from_file('students.src')
# [print(el) for el in students]

print('*' * 25)
students = Student.import_from_file('students.src')
group = Group('13')
group.add_students(students)
[print(el, el.group) for el in students]


print('*' * 25)
librarians = Librarian.import_from_file('librarians.src')
[print(el) for el in librarians]

print('*' * 25)
teachers = Teacher.import_from_file('teachers.src')
[print(el) for el in teachers]


