# commands.py

import sys
from datetime import datetime
from .utils import add_person, list_people, select_people_by_month, exit_program, help_info


def main():
    people = []

    while True:
        command = input(">>> ").lower()

        match command:
            case 'exit':
                exit_program()
            case 'add':
                add_person(people)
            case 'list':
                list_people(people)
            case command if command.startswith('select '):
                month_to_search = int(command.split(' ')[1])
                select_people_by_month(people, month_to_search)
            case 'help':
                help_info()
            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
