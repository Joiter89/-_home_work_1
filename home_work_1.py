class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def middle(self):
        self.grade_student = []
        for v in self.grades.values():
            self.grade_student.extend(v)
        middle_grade = round(sum(self.grade_student) / len(self.grade_student), 2)  
        return middle_grade
    def __str__(self):
        print('Имя студента:', self.name,'\nФамилия студента:', self.surname, '\nСредняя оценка за домашние задания:', self.middle(), '\nКурсы в процессе изучения:', self.courses_in_progress, '\nЗавершенные курсы:', self.finished_courses)  
        return 
    def __lt__(self, other):
        if self.middle() > other.middle():
            print('Лучший студент -', self.name, self.surname)
        else: 
            print('Лучший студент -', other.name, other.surname)
        return
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def middle(self):
        self.grade_lecture = []
        for v in self.grades.values():
            self.grade_lecture.extend(v)
        middle_grade = round(sum(self.grade_lecture) / len(self.grade_lecture), 2)
        return middle_grade
    def __str__(self):
        res = print('Имя лектора:', self.name, '\nФамилия лектора:', self.surname, '\nСредняя оценка за лекции:', self.middle())
        return res
    def __lt__(self, other):
        if self.middle() > other.middle():
            print('Лучший лектор -', self.name, self.surname)
        else:
            print('Лучший лектор -', other.name, other.surname)        
        return  
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
        print('Имя эксперта:', self.name, '\nФамилия эксперта:', self.surname)
        return 

first_student = Student('Петр', 'Гавриков', 'мужчина')
second_student = Student('Татьяна','Фролова', 'женщина')
first_student.courses_in_progress += ['Python', 'Git']
second_student.courses_in_progress += ['Python', 'Git']
first_student.finished_courses += ['Pascal']
second_student.finished_courses += ['Math']

first_mentor = Mentor('Федор','Прокопьев')
second_mentor = Mentor('Тамара', 'Щаулина')
first_mentor.courses_attached += ['Python', 'Git']
second_mentor.courses_attached += ['Python', 'Git']

first_lecturer = Lecturer('Антон', 'Ратников')
second_lecturer = Lecturer('Максим', 'Мушкетов')
first_lecturer.courses_attached += ['Python', 'Git']
second_lecturer.courses_attached += ['Python', 'Git']

first_reviewer = Reviewer('Владимир', 'Медведев')
second_reviewer = Reviewer('Алексей', 'Астахов')
first_reviewer.courses_attached += ['Python', 'Git']
second_reviewer.courses_attached += ['Python', 'Git']

first_student.rate_hw(first_lecturer, 'Python', 91)
first_student.rate_hw(first_lecturer, 'Python', 93)
first_student.rate_hw(first_lecturer, 'Python', 77)
first_student.rate_hw(first_lecturer, 'Git', 71)
first_student.rate_hw(first_lecturer, 'Git', 80)
first_student.rate_hw(first_lecturer, 'Git', 69)
second_student.rate_hw(second_lecturer, 'Python', 81)
second_student.rate_hw(second_lecturer, 'Python', 98)
second_student.rate_hw(second_lecturer, 'Python', 84)
second_student.rate_hw(second_lecturer, 'Git', 91)
second_student.rate_hw(second_lecturer, 'Git', 88)
second_student.rate_hw(second_lecturer, 'Git', 84)

first_reviewer.rate_hw(first_student, 'Python', 89)
first_reviewer.rate_hw(first_student, 'Python', 93)
first_reviewer.rate_hw(first_student, 'Python', 99)
first_reviewer.rate_hw(first_student, 'Git', 80)
first_reviewer.rate_hw(first_student, 'Git', 83)
first_reviewer.rate_hw(first_student, 'Git', 89)
second_reviewer.rate_hw(second_student, 'Python', 85)
second_reviewer.rate_hw(second_student, 'Python', 72)
second_reviewer.rate_hw(second_student, 'Python', 78)
second_reviewer.rate_hw(second_student, 'Git', 81)
second_reviewer.rate_hw(second_student, 'Git', 60)
second_reviewer.rate_hw(second_student, 'Git', 74)

first_student.__str__()
second_student.__str__()
first_student.__lt__(second_student)

first_lecturer.__str__()
second_lecturer.__str__()
first_lecturer.__lt__(second_lecturer)

first_reviewer.__str__()
second_reviewer.__str__()

student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]

def middle_grade_student(student_list, course):
    overal_grades = 0
    count_grades = 0
    for student in student_list:
        if course in student.grades.keys():
            for grades in student.grades[course]:
                overal_grades += grades
            count_grades += len(student.grades[course])
    print('Средняя оценка по курсу', course, 'у студентов составляет:', round(overal_grades / count_grades, 2))
    return  
  
middle_grade_student(student_list, 'Python') 
middle_grade_student(student_list, 'Git') 

def middle_grade_lecturer(lecturer_list, course):
    overal_grades = 0
    count_grades = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades.keys():
            for grades in lecturer.grades[course]:
                overal_grades += grades
            count_grades += len(lecturer.grades[course])
    print('Средняя оценка по курсу', course, 'у лекторов составляет:', round(overal_grades / count_grades, 2))
    return 
  
middle_grade_lecturer(lecturer_list, 'Python')
middle_grade_lecturer(lecturer_list, 'Git') 