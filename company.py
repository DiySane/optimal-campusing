class Company:
    count = 0

    def __init__(self):
        Company.count += 1
        self.id = Company.count
        self.name = "C-"+str(self.id)
        self.preferences = set()

    def __str__(self):
        return self.name + ' [' + ','.join(str(preference) for preference in self.preferences) + ']'
