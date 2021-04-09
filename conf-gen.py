import random
from pathlib import Path
from datetime import datetime
from os import system, name


def clear():
    if name == 'nt':
        return system('cls')
    else:
        return system('clear')


def getutc():
    now = datetime.utcnow().strftime("%H_%M_%S")
    return str(now)


def randver():
    major = random.randint(0, 48)
    minor = random.randint(1, 9)
    return str(major), str(minor)


def user_setup():
    # Get names of files in templates directory
    template_dir = 'templates'
    templates = (x for x in Path(template_dir).iterdir() if x.is_file())
    for template in templates:
        template = Path(template).name
        print(template)

    # Get user provided name of template file
    template_input = input('\nWhat template would you like to use? ')
    template = Path(template_dir + '/' + template_input)
    template = template.absolute()

    # Set the name of the output file
    base = template.stem
    output_file = Path(base + '_output_' + getutc() + "Z.txt").absolute()
    return template, output_file


def main():
    # Formatting
    clear()
    print('Available templates:\n==============')

    template, output_file = user_setup()

    # List of user supplied information to replace
    ip1 = input('IP: ')
    maj_ver, min_ver = randver()

    # Loops through each line to replace variables
    with template.open('rt') as tf:
        with output_file.open('wt') as of:
            for line in tf:
                of.write(line.replace('$ip1', ip1)
                         .replace('$maj_ver', maj_ver)
                         .replace('$min_ver', min_ver)
                         )


if __name__ == '__main__':
    main()
