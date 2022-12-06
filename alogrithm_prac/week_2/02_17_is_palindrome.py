input = "abcba"

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:     # stinrg[-1] 은 문장의 마지막 단어
        return False
    return is_palindrome(string[1:-1])  # 첫번째 문자열과 마지막 문자열 잘라서 출력

print(is_palindrome(input))