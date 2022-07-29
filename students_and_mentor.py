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

    def __lt__(self, other):
        print('Сравниваем у двух студентов оценки за домашнее задание')
        return  self.home_work_grades == other.home_work_grades


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


# Task-2
# cool_lecturer = Lecturer('Vovan', 'Tolyan', "Python")
# cool_lecturer.courses_attached += ['Python']
#
# cool_lecturer.rate_lec(cool_lecturer, 'Python', 10)
# cool_lecturer.rate_lec(cool_lecturer, 'Python', 9)
# print(cool_lecturer.name, cool_lecturer.grades)

# Task-3


# print(cool_reviewer)
# print("========================================")
# print(cool_lecturer)
#
# print("========================================")
# print(best_student)

# Class instances
# class Student
student1 = Student('Maria', 'Mashkova', "woman")
student1.grades = {'Python': [5, 10, 7, 8, 10], 'javascript': [9, 10, 9, 8, 10]}
student1.home_work_grades = [10, 7, 8, 9, 10]
student1.finished_courses = ['Основы программирования']
student1.courses_attached = ['Python', 'javascript']

student2 = Student('Pol', 'Haris', "man")
student2.home_work_grades = [10, 9, 9, 9, 10]
student2.grades = {'Python': [5, 10, 7, 8, 10], 'javascript': [8, 10, 8, 8, 9]}
student2.finished_courses = ['Основы программирования', 'Git', 'C++']
student2.courses_attached = ['Python', 'javascript', ]

# class Mentor
mentor1 = Mentor('Bob', 'Dol', 'Git')
mentor2 = Mentor('Muhamed', 'Ali', 'Python')

# class Lecturer
lecturer1 = Lecturer('Vlad', 'Stashevski', 'Python')
lecturer1.grades = {'Python': [10, 9, 10, 8, 10]}
lecturer1.courses_attached += ["Python"]
lecturer2 = Lecturer('Vladimir', 'klyar', 'Git')
lecturer2.grades = {'Git': [10, 5, 10, 10, 7]}
lecturer2.courses_attached += ["Git"]

# class Reviewer
reviewer1 = Reviewer('Yarik', 'Bull', 'Python')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Sasha', 'Klinton', 'Python')

# Вызов методов
# print(student1.rate_lec(lecturer1, 'Python', '10'))
# print(student2.rate_lec(lecturer2, 'Python', '10'))
# print(student1.average_rating())
# print(student2.average_rating())
# print(lecturer1.average_rating())
# print(reviewer1.rate_hw(student1, "Python", 9))


# print(dir(cool_lecturer))
# print(cool_lecturer.__dict__)
# print(cool_lecturer.__str__())


# Magical methods
# print(student2.__str__())
# print(student1.__str__())
# print(lecturer1.__str__())
# print(lecturer2.__str__())
# print(reviewer2.__str__())
# print(reviewer1.__str__())
print(student1.__lt__(student2))


