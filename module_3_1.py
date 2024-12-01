calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    qwe = [(len(string)), string.upper(), string.lower()]
    qwe = tuple(qwe)
    return qwe

def is_contains(string, list_to_search):
    count_calls()
    zxc = []
    for i in list_to_search:
        zxc.append(i.lower())
    qaz = string.lower() in zxc
    return qaz



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)