class Combo:
    def __init__(self, student, company):
        self.student = student
        self.company = company

    def __str__(self):
        return '(' + str(self.student.name) + ', ' + str(self.company.name) + ')'

    def __eq__(self, other):
        return str(self) == str(other)
        # return str(self.student) == str(other.student) and str(self.company) == str(other.company)

    def __hash__(self):
        return hash(str(self))