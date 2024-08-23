calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())



def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

print(string_info('Flower'))
print(string_info('Wind'))
print(is_contains('Urban', ['ban', 'BaNaN']))
print(is_contains('cycle', ['recycling', 'cyclic', 'CYclE']))
print(calls)
