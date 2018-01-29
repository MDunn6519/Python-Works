import string

def get_personal_data() -> dict:
    """"
    :return: Returns personal data
    """

    personal_data = {"name": "Matt", "A_Role": "Student"}
    return personal_data


def main() -> int:
    default_dict = dict()
    print(default_dict)
    initialized_dict = dict([('name', 'matt'), ('a_role', 'student')])
    print(initialized_dict)
    simple_init_dict = dict(name='matt', a_role='student')
    print(simple_init_dict)
    simple_init_dict['a_role'] = 'joker'
    print(simple_init_dict)
    my_comprehension = {x: x**2 for x in range(5)}
    print(my_comprehension)

    s = "a little lamb, it's fleece".translate({ord(i): None for i in string.punctuation}).split()
    print(s)
    return 0


if __name__ == '__main__':
    main()
