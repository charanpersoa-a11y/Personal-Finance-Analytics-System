class User:
    def __init__(self, name, age, email, password):

        self.name = name
        self.age = age
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, user_id, data):
        return cls(user_id, data["name"], data["age"], data["email"], data["password"])

