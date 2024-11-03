class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_subject(self, subject, mark):
        self.marks[subject] = mark

    def total_marks(self):
        total = sum(self.marks.values())
        return total

    def percentage(self):
        total_obtained = self.total_marks()
        max_marks = len(self.marks) * 100
        percentage = (total_obtained / max_marks) * 100 if max_marks > 0 else 0
        return percentage


if __name__ == '__main__':
    student1 = Student("Bob")
    student2 = Student("Mary")
    student1.add_subject("Math", 61)
    student1.add_subject("Physics", 76)
    student2.add_subject("Physics", 82)
    student2.add_subject("Chemistry", 90)

    print(f"Total marks = {student1.total_marks()}")
    print(f"Percentage = {student1.percentage():.2f}%")

    print(f"Total marks = {student2.total_marks()}")
    print(f"Percentage = {student2.percentage():.2f}%")