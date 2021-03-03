class Student:
    count = 0

    # def __init__(self, name):
    #     Student.count += 1
    #     self.id = Student.count
    #     self.name = name

    def __init__(self):
        Student.count += 1
        self.id = Student.count
        self.name = "S-"+str(self.id)
        self.preferences = set()

    def __str__(self):
        return self.name + ' [' + ','.join(str(preference) for preference in self.preferences) + ']'
