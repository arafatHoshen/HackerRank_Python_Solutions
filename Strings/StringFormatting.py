"""
Title     : String Formatting
Subdomain : Strings
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""
def print_formatted(number):
    w=len(str(bin(number))[2:])
    for i in range(1,number+1):
        print(str(i).rjust(w,' '),oct(i)[2:].rjust(w,' '),hex(i)[2:].upper().rjust(w,' '),bin(i)[2:].rjust(w,' '))