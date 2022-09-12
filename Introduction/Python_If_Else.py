"""
Title     : Python If-Else
Domain    : Python
Subdomain : Introduction
Author    : Arafat Hoshen
Created   : 12 September 2022
Problem   : https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
Visit My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""
n = int(input())
if n % 2 == 1 or n in range(5,21):
    print("Weird")
else:
    print("Not Weird")