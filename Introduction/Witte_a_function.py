"""
Title           : Python Write a function
Domain          : Python
Subdomain       : Introduction
Author          : Arafat Hoshen
Created         : 12 September 2022
Problem         : https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
Visit My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""
def is_leap(year):
    leap = False
    leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return leap
year = int(input())