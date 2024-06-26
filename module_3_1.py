
def count_calls():
    global calls
    calls = calls + 1

    return calls
def string_info(a):
    count_calls()
    b = (len(a), a.upper(), a.lower())
    return b

def is_contains(string, list):
    count_calls()
    list1 = [string.lower() for string in list]
    if string.lower() in list1:
        return True
    else:
        return False

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)