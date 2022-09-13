"""
Title           : Tuples
Domain          : Python
Subdomain       : Introduction
Author          : Arafat Hoshen
Created         : 14 September 2022
Problem         : https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
Visit My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""
n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))