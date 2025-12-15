import json
from services.models import Student

class StudentRepository:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def load(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Student.from_dict(s) for s in data["students"]]

    def save(self, students):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                {"students": [s.to_dict() for s in students]},
                f,
                indent=2
            )

    def upsert(self, student):
        students = self.load()
        students = [s for s in students if s.nim != student.nim]
        students.append(student)
        self.save(students)

    def delete(self, nim):
        students = self.load()
        students = [s for s in students if s.nim != nim]
        self.save(students)
