from schemas.student import StudentCreate, StudentUpdate, StudentPatch

students = {}

next_student_id = 1


def create_student(student: StudentCreate):
    global next_student_id

    student_data = student.model_dump()
    student_data["id"] = next_student_id

    students[next_student_id] = student_data

    created_student = students[next_student_id]
    next_student_id += 1

    return created_student


def get_all_students():
    return list(students.values())


def get_student(student_id: int):
    return students.get(student_id)


def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students:
        return None

    student_data = student.model_dump()
    student_data["id"] = student_id

    students[student_id] = student_data

    return students[student_id]


def patch_student(student_id: int, student: StudentPatch):
    if student_id not in students:
        return None

    update_data = student.model_dump(exclude_unset=True)

    students[student_id].update(update_data)

    return students[student_id]


def delete_student(student_id: int):
    if student_id not in students:
        return False

    del students[student_id]

    return True