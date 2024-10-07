class NameError(Exception):
    pass


class EmailError(Exception):
    pass


class AgeError(Exception):
    pass


def check_name(name):
    words = str(name).split()
    if len(words) >= 2:
        for word in words:
            if str(word).istitle():
                pass
            else:
                return False
    else:
        return False
    return True


def check_email(email):
    if "@." in email:
        return True


def check_age(age):
    if 0 < int(age) < 120:
        return True


class User:
    def __init__(self, name, email, age):
        if check_name(name):
            self.name = name
        else:
            raise NameError("Name has to contain at least two words and begin with capital letter.")
        if check_email(email):
            self.email = email
        else:
            raise EmailError("An email has to contain symbols '@' and '.'")
        if check_age(age):
            self.age = age
        else:
            raise AgeError("An age has to be between 1 and 120.")

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


if __name__ == '__main__':
    u1 = User('Harry Potter', "hp@.com", 12)
    print(u1)
