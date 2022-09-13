"""
Title           : Find the Runner-Up Score!
Domain          : Python
Subdomain       : Introduction
Author          : Arafat Hoshen
Created         : 14 September 2022
Problem         : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
Visit My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])