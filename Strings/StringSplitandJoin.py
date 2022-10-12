"""
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""

def split_and_join(sentence):
    return "-".join(sentence.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)