condition = True


def change_condition():
    global condition
    condition = False


def get_condition():
    print(condition)
    return condition
