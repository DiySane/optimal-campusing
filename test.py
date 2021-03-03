from coolname import generate_slug
import random
import json

from company import Company
from student import Student
from combo import Combo

students = []
companies = []
combos_dict = dict()
time_slots = []
time_slot_students_dict = dict()
time_slot_company_student_dict = dict()


def get_random_number(floor, ceil):
    return random.randint(floor, ceil)


def get_random_name():
    return generate_slug(2).split("-")[1]


def init_companies(m):
    for i in range(m):
        companies.append(Company())


def init_students(n):
    for i in range(n):
        students.append(Student())


def init_time_slots(t):
    for i in range(t):
        time_slots.append(i+1)
        time_slot_company_student_dict[i+1] = dict()
        time_slot_students_dict[i+1] = set()


def init_company_preferences():
    for company in companies:
        number_of_preferences = random.randint(1, len(students)//2)
        for i in range(number_of_preferences):
            random_student_id = random.randint(1, len(students) - 1)
            company.preferences.add(random_student_id)


def init_student_preferences():
    for student in students:
        number_of_preferences = random.randint(1, len(companies)//2)
        for i in range(number_of_preferences):
            random_company_id = random.randint(1, len(companies) - 1)
            student.preferences.add(random_company_id)


def create_combos():
    for student in students:
        for preference in student.preferences:
            preferred_company = companies[preference - 1]
            combo = Combo(student, preferred_company)
            if(combo not in combos_dict.keys()):
                combos_dict[combo] = 1
            else:
                combos_dict[combo] += 1
    for company in companies:
        for preference in company.preferences:
            preferred_student = students[preference - 1]
            combo = Combo(preferred_student, company)
            if(combo not in combos_dict.keys()):
                combos_dict[combo] = 1
            else:
                combos_dict[combo] += 1


def by_value(item):
    return item[1]


def sort_combos():
    sorted_combos = dict()
    for k, v in sorted(combos_dict.items(), key=by_value, reverse=True):
        sorted_combos[k] = v
    # combos_dict = sorted_combos
    return sorted_combos

# def fill_slots(sorted_combos):
#     for combo in sorted_combos.keys():
#         for slot in time_slots:
#             if (combo.student not in time_slot_students_dict.get(slot) and combo.company not in time_slot_company_student_dict.get(slot).keys()):
#                 time_slot_students_dict[slot].add(combo.student)
#                 time_slot_company_student_dict[slot][combo.company] = combo.student


def fill_slots(sorted_combos):
    for combo in sorted_combos.keys():
        for slot in time_slots:
            if (combo.student.name not in time_slot_students_dict.get(slot) and combo.company.name not in time_slot_company_student_dict.get(slot).keys()):
                time_slot_students_dict[slot].add(combo.student.name)
                time_slot_company_student_dict[slot][combo.company.name] = combo.student.name
                break


def main():
    number_of_companies = 12
    number_of_students = 24
    init_companies(number_of_companies)
    init_students(number_of_students)
    # print(', '.join(str(company) for company in companies))
    # print(', '.join(str(student) for student in students))
    print(Company.count)
    print(Student.count)
    init_company_preferences()
    init_student_preferences()
    print(', '.join(str(company) for company in companies))
    print(', '.join(str(student) for student in students))

    print("\n-----------------------------------\n")

    create_combos()
    sorted_combos = sort_combos()
    print(' \n '.join(str(key) + ': ' + str(value)
                      for key, value in sorted_combos.items()))

    print("\n-----------------------------------\n")

    init_time_slots(10)
    # print(time_slots)
    # print(time_slot_students_dict)

    fill_slots(sorted_combos)
    json_object = json.dumps(time_slot_company_student_dict, indent=4)
    print(json_object)


if __name__ == "__main__":
    main()
