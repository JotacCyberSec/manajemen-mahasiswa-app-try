from dataclasses import dataclass

@dataclass
class Student:
    _nim: str
    _name: str
    _email: str
    _major: str

    @property
    def nim(self): return self._nim
    @property
    def name(self): return self._name
    @property
    def email(self): return self._email
    @property
    def major(self): return self._major

    def to_dict(self):
        return {
            "nim": self.nim,
            "name": self.name,
            "email": self.email,
            "major": self.major
        }

    @staticmethod
    def from_dict(d):
        return Student(d["nim"], d["name"], d["email"], d["major"])
