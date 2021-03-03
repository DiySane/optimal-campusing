import random
import json

from company import Company
from student import Student
from combo import Combo


class Test:

    def __init__(self, number_of_companies, number_of_students, number_of_slots):
        self.init_empties()
        self.init_companies(number_of_companies)
        self.init_students(number_of_students)
        self.init_time_slots(number_of_slots)
        self.init_company_preferences()
        self.init_student_preferences()
        self.create_combos()
        self.sort_combos()
        self.fill_slots()

    def init_empties(self):
        self.time_slots = []
        self.time_slot_students_dict = dict()
        self.time_slot_company_student_dict = dict()
        self.combos_dict = dict()
        self.sorted_combos = dict()

    def init_companies(self, m):
        self.companies = [Company() for _ in range(m)]

    def init_students(self, n):
        self.students = [Student() for _ in range(n)]

    def init_time_slots(self, t):
        for i in range(t):
            self.time_slots.append(i+1)
            self.time_slot_company_student_dict[i+1] = dict()
            self.time_slot_students_dict[i+1] = set()

    def init_company_preferences(self):
        for company in self.companies:
            number_of_preferences = random.randint(1, len(self.students)//2)
            for _ in range(number_of_preferences):
                random_student_id = random.randint(1, len(self.students) - 1)
                company.preferences.add(random_student_id)

    def init_student_preferences(self):
        for student in self.students:
            number_of_preferences = random.randint(1, len(self.companies)//2)
            for _ in range(number_of_preferences):
                random_company_id = random.randint(1, len(self.companies) - 1)
                student.preferences.add(random_company_id)

    def create_combos(self):
        for student in self.students:
            for preference in student.preferences:
                preferred_company = self.companies[preference - 1]
                combo = Combo(student, preferred_company)
                if(combo not in self.combos_dict.keys()):
                    self.combos_dict[combo] = 1
                else:
                    self.combos_dict[combo] += 1
        for company in self.companies:
            for preference in company.preferences:
                preferred_student = self.students[preference - 1]
                combo = Combo(preferred_student, company)
                if(combo not in self.combos_dict.keys()):
                    self.combos_dict[combo] = 1
                else:
                    self.combos_dict[combo] += 1

    def by_value(self, item):
        return item[1]

    def sort_combos(self):
        for k, v in sorted(self.combos_dict.items(), key=self.by_value, reverse=True):
            self.sorted_combos[k] = v

    def fill_slots(self):
        for combo in self.sorted_combos.keys():
            for slot in self.time_slots:
                '''Check if either student or company is visited
                for the given slot.
                '''
                if (combo.student.name not in self.time_slot_students_dict.get(slot) and combo.company.name not in self.time_slot_company_student_dict.get(slot).keys()):
                    '''Mark the student entry visited for the specific time-slot, 
                    as one student can't attend two sessions simultaneously'''
                    self.time_slot_students_dict[slot].add(combo.student.name)
                    '''Add the student entry for a slot-company combination, 
                    append the priority as well for better legibility.
                    This will mark the company visited for the slot too.'''
                    self.time_slot_company_student_dict[slot][combo.company.name] = combo.student.name + ', ' + str(
                        self.sorted_combos[combo])
                    break


def main():
    # test = Test(20, 40, 15)
    test = Test(5, 10, 8)
    json_object = json.dumps(test.time_slot_company_student_dict, indent=4)
    print(json_object)


if __name__ == "__main__":
    main()
