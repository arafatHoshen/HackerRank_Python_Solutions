"""
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
"""


def swap_case(sentence):
    updated_s = ""
    for c in sentence:
        if c.isupper():
            updated_s += c.lower()
        elif c.islower():
            updated_s += c.upper()
        else:
            updated_s += c
    return updated_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)