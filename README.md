Home work consists of 2 tasks

# Task 1. Create a function to display a list of colleagues who need to be congratulated on their birthday in the week.

## Description

File name `get_birthdays_per_week.py`. The file contains a function `get_birthdays_per_week` that's called with a list of dictionaries. Each dictionary must have such required keys as `name` and `birthday`.

Example of a dictionary:

```
{"name": "Bill Gates", "birthday": datetime(1955, 11, 11)}
```

The function `get_birthdays_per_week`` outputs the names of birthday people in the following format:

```
Monday: Bill Gates, Jill Valentine
Friday: Kim Kardashian, Jan Koum
```

## How to run

Example of the function call:

```
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 11, 11)},
    {"name": "Jill Valentine", "birthday": datetime(1955, 11, 12)},
    {"name": "Kim Kardashian", "birthday": datetime(1955, 11, 10)},
    {"name": "Jan Koum", "birthday": datetime(1955, 11, 10)},
]

get_birthdays_per_week(users)

```

# Task 2. Create an assistant console Bot that will recognize commands entered from the keyboard and respond accordingly.

## Description

File name `bot.py`. The file contains a main function and be called dirrectly from the console `python bot.py`.

Basic commands:

```
hello                - used to show a welcome message
add                  - used to add a new contact: "add username phone"
change               - used to change a contact phone number: "change username phone"
phone                - used to show a phone number: "phone username"
all                  - used to show all saved contacts with phone numbers
help                 - used to show commands
close or exit        - used to terminate the program
```

If the command was not recognized, the following message will be displayed

```
Invalid command. Type "help" to see a list of commands.
```

If not enough arguments were entered, the following message will be displayed, indicating the required number of arguments.

```
Not enough values, expected 2.
```

## How to run

Example of the Bot call:

```
python bot.py
```

In order to terminate the Bot use "close" or "exit" command.

```
Enter a command: close
Good bye!
```

## Modules

The folder `bot_utils` contains all the important utilities for the Bot to work.
