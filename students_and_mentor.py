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
        self.home_work_grades = []

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        aver = sum(self.home_work_grades) / len(self.home_work_grades)
        return aver

    def __str__(self):
        rez = self.average_rating()
        return f"Student \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {rez} \n" \
               f"Курсы в процессе изучения: {(', '.join(self.courses_attached))} \nЗавершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.courses_attached = []


class Lecturer(Mentor, Student):
    grades = {}

    def average_rating(self):
        aver = sum(self.grades[self.course]) / len(self.grades[self.course])
        return aver

    def __str__(self):
        rez = self.average_rating()
        return f"lecturer \nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {rez} "


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Reviewer \nИмя: {self.name} \nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.home_work_grades = [8, 10, 6, 9]
best_student.courses_attached = ['Python', 'Git']
best_student.finished_courses = "Введение в программирование"
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy', "Python")
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)

# Task-2
cool_lecturer = Lecturer('Vovan', 'Tolyan', "Python")
cool_lecturer.courses_attached += ['Python']

cool_lecturer.rate_lec(cool_lecturer, 'Python', 10)
cool_lecturer.rate_lec(cool_lecturer, 'Python', 10)
# print(cool_lecturer.name, cool_lecturer.grades)

# Task-3


print(cool_reviewer)
print("========================================")
print(cool_lecturer)

print("========================================")
print(best_student)
