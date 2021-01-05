class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        students_as_string = ", ".join(self.students)
        grade = self.get_average_grade()
        return f"The students in {self.name}: {students_as_string}. Average grade: {grade:.2f}"
