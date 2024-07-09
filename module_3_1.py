# 1
calls = 0


# 2
def count_calls():
    global calls
    calls += 1


# 3
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


# 4
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('KoloBorashion'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('Univer', ['UniVer', 'ver', 'uni']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(is_contains('Univer', ['SoUniver', 'ver', 'uni']))
print(calls)

