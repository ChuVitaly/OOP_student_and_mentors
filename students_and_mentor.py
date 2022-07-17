"""
Задание:
теперь класс Mentor должен стать родительским классом, а от него нужно реализовать наследование классов Lecturer
(лекторы)и Reviewer (эксперты, проверяющие домашние задания).
 Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.
"""


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):
    grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)

# Task-2
cool_lecturer = Lecturer('Vovan', 'Tolyan')
cool_lecturer.courses_attached += ['Python']

cool_lecturer.rate_lec(cool_lecturer, 'Python', 10)
cool_lecturer.rate_lec(cool_lecturer, 'Python', 10)
print(cool_lecturer.name, cool_lecturer.grades)
