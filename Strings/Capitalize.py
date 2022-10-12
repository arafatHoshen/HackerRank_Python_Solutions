'''
Title     : Capitalize!
Subdomain : Strings
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
'''
def solve(s):
    return ' '.join(i.capitalize()   for i in s.split(' '))
