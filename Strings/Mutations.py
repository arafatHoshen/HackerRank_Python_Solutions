"""
Title     : Mutations
Subdomain : Strings
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""

def mutate_string(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)