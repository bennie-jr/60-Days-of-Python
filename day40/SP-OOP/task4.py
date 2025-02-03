class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        pass


    def age(self, current_year):
        user_age = current_year - self.birthyear
        return user_age


user = User(name="John", birthyear=1999)
print(user.age(2023))

# User(name="John", birthyear=1999).age(current_year=2023)