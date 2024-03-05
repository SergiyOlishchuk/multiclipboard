import json
import clipboard
import os

def exist_file():
    file = open('clipboard.json', 'a')
    file.close()

def add_to_file(inform):
    with open('clipboard.json') as file:
        try:
            cb = json.load(file)
            cb.update(inform)
        except:
            cb = inform

    with open('clipboard.json', 'w') as file:
        file.write(json.dumps(cb))


def get_from_file(key):
    with open('clipboard.json') as file:
        try:
            cb = json.load(file)
        except:
            return None

    res = cb.pop(key, None)

    if res:
        with open('clipboard.json', 'w') as file:
            file.write(json.dumps(cb))

    return res

def get_all_from_file() -> dict:
    with open('clipboard.json') as file:
        try:
            return json.load(file)
        except:
            return {}


def clear_file():
    file = open('clipboard.json', 'w')
    file.close()

def main():
    print('Welcome to multiclipboard!!!\n')
    
    exist_file()

    cb = get_all_from_file()

    if len(cb.keys()) == 0:
        print('Multiclipboard is empty.\n')
        print('1 - add record')
        print('2 - exit')

        info = input()

        if info == '2':
            return

        record = input('Enter name of record: ')

        add_to_file({record : clipboard.paste()})

    else:
        i = 1
        for key in cb.keys():
            print(str(i) + '. ' + key)
            i += 1

        print()

        print('1 - add record')
        print('2 - load record')
        print('3 - clear clipboard')
        print('4 - exit')

        info = input()

        if info == '4':
            return
        elif info == '1':
            record = input('Enter name of record: ')

            add_to_file({record : clipboard.paste()}) 
        elif info == '2':
            name = input('Enter name of record: ')

            record = get_from_file(name)

            if record:
                clipboard.copy(record)
            else:
                print('Invalid name')

        elif info == '3':
            clear_file()

if __name__ == '__main__':
    main()