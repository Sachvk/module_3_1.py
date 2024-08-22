calls = 0


def count_calls(calls):
    print(calls)


def string_info(string):
    global calls
    calls += 1
    a = (len(string), string.upper(), string.lower())
    return a


def is_contains(string, list_to_search):
    global calls
    calls += 1
    for item in list_to_search:
        b = []
        b.append(item.lower())
    if string.lower() in b:
        return True
    else:
        return False


print(string_info('Flower'))
print(string_info('Wind'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
