import re

def validate_student_payload(data):
    nim = data.get("nim", "").strip()
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    major = data.get("major", "").strip()

    if not re.match(r"^\d{8,15}$", nim):
        raise ValueError("NIM harus 8–15 digit")

    if len(name) < 2:
        raise ValueError("Nama minimal 2 karakter")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Email tidak valid")

    if len(major) < 2:
        raise ValueError("Jurusan minimal 2 karakter")

    return {
        "nim": nim,
        "name": name,
        "email": email,
        "major": major
    }
