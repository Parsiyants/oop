def calc_average_score(list: list, course: str) -> float:
    average_score = 0
    if list:
        for item in list:
            if isinstance(item, Student):
                if course in item.courses_in_progress:
                    average_score += item.average_rate()
            elif isinstance(item, Lecturer):
                if course in item.courses_attached:
                    average_score += item.average_rate()
        # и получаем общую среднюю оценку по курсу для всех студентов
        return round(average_score / len(list), 2)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.students_grade:
                lecturer.students_grade[course] += [grade]
            else:
                lecturer.students_grade[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n' \
            f'Средняя оценка за домашние задания: {self.average_rate()}\n' \
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
            f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def average_rate(self):
        grade = []
        for key, value in self.grades.items():
            for num in value:
                grade.append(num)
        average = sum(grade) / len(grade)
        return average
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории людей не сравниваем.")
            return
        return self.average_rate() < other.average_rate()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.students_grade = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
            f'Фамилия: {self.surname}\n' \
            f'Средняя оценка за лекции: {self.average_rate()}\n'
    
    def average_rate(self):
        grade = []
        for key, value in self.students_grade.items():
            for num in value:
                grade.append(num)
        average = sum(grade) / len(grade)
        return average
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Разные категории людей не сравниваем.")
            return
        return self.average_rate() < other.average_rate()

# Пример 1
lecturer = Lecturer('Mentor', 'Lecturer')
lecturer.courses_attached += ['Python']

student = Student('Tigran', 'Parsiyants', 'male')
student.courses_in_progress += ['Python']
student.rate_lecturer(lecturer, 'Python', 10)

reviewer = Reviewer('Mentor', 'Reviewer')
reviewer.courses_attached += ['Python']
reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student, 'Python', 10)

# Пример 2
lecturer2 = Lecturer('Mentor2', 'Lecturer2')
lecturer2.courses_attached += ['Python']

student2 = Student('Tigran2', 'Parsiyants2', 'male')
student2.courses_in_progress += ['Python']
student2.rate_lecturer(lecturer2, 'Python', 9)

reviewer2 = Reviewer('Mentor2', 'Reviewer2')
reviewer2.courses_attached += ['Python']
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 5)


# Примеры по заданием №1-3
print(student, reviewer, lecturer)
print(student2, reviewer2, lecturer2)

# Пример со сравнением
print(student.__lt__(student2))
print(lecturer.__lt__(lecturer2))

#Задание № 4, для подсчёта средней оценки студентов и лекторов в рамках конкретного курса
print(calc_average_score([student, student2], 'Python'))
print(calc_average_score([lecturer, lecturer2], 'Python'))


