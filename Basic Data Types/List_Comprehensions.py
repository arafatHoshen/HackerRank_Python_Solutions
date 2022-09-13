"""
Title           : List Comprehensions
Domain          : Python
Subdomain       : Introduction
Author          : Arafat Hoshen
Created         : 14 September 2022
Problem         : https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
Visit My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arafat = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in
          range(z + 1) if i + j + k != n]
    print(arafat)