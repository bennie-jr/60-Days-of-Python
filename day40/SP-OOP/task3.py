class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        pass


    def age(self, current_year):
        user_age = current_year - self.birthyear
        return user_age
