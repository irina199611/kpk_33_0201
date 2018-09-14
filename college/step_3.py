from college import Human, Student, Group

student_1 = Student('Игнатьев', 'Петр', 'Ильич')
student_2 = Student('Перов', 'Василий', 'Петрович')
student_3 = Student('Васильев', 'Илья', 'Васильевич')
student_4 = Student('Смирнов', 'Алексей', 'Сергеевич')
student_5 = Student('Тишков', 'Денис', 'Валерьевич')
student_6 = Student('Игнатова', 'Ольга', 'Викторовна')
student_7 = Student('Сафронова', 'Екатерина', 'Алексеевна')
print(student_1)


group_1 = Group('33', 'Прикладная информатика 09.02.05')
group_2 = Group('23', 'Прикладная информатика 09.02.05')
# группа: "33" (09.02.05)
# print(group_1)
student_1.set_group(group_1)
student_2.set_group(group_2)
student_3.set_group(group_1)
student_4.set_group(group_2)
student_5.set_group(group_1)
student_6.set_group(group_2)
student_7.set_group(group_1)

students = [student_1, student_2, student_3, student_4, student_5, student_6, student_7]

# print(student_1.group)
print(f'\nВ мероприятии участвовали:')
for student in students:
    print(f'\t{student} ({student.group})')

