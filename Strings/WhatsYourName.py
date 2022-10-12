"""
Title     : Whats Your Name?
Subdomain : Introduction
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)