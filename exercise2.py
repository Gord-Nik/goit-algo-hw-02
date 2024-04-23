from collections import deque


def check_string(some_text: str) -> bool:
    refactored_str = some_text.replace(" ", "").lower()
    queue = deque(refactored_str)

    for i in range(len(refactored_str) // 2):
        if queue.pop() != queue.popleft():
            print("Word is not a palindrome")
            return False

    print("Word is a palindrome")
    return True


if __name__ == "__main__":
    check_string("дед")
    check_string("а роза упала на лапу Азора")
    check_string("обормот")
    check_string("ВаСиЛич")
    check_string("Аргентина маНит неГра")
