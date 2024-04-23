import re


def validate_brackets(expression: str) -> str:
    brackets_map = {'(': ')', '[': ']', '{': '}'}
    open_brackets = brackets_map.keys()
    stack = []

    for char in expression:
        if char in open_brackets:  # Якщо символ є відкритою скобкою
            stack.append(char)
        elif char in brackets_map.values():  # Якщо символ є закритою скобкою
            if not stack:
                return "Несиметричні скобки"
            current_open = stack.pop()
            if brackets_map[current_open] != char:
                return f"Невідповідність скобок: очікувалась {brackets_map[current_open]}, але знайдено {char}"

    if stack:
        return "Несиметричні скобки"
    return "Скобки симетричні"


if __name__ == "__main__":
    print(validate_brackets("( ){[ ]( )( ) { } }"))
    print(validate_brackets("([)]"))
    print(validate_brackets("((()"))
