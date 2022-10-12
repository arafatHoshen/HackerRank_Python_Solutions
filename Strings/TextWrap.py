"""
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)