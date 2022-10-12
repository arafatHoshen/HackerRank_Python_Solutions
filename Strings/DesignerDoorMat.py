"""
Title     : Designer Door Mat
Subdomain : Strings
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""
N, M = map(int, input().split())
for i in range(1, N, 2):
    print(int((M - 3 * i) / 2) * '-' + (i * '.|.') + int((M - 3 * i) / 2) * '-')
print(int((M - 7) / 2) * '-' + 'WELCOME' + int((M - 7) / 2) * '-')
for i in range(N - 2, -1, -2):
    print(int((M - 3 * i) / 2) * '-' + (i * '.|.') + int((M - 3 * i) / 2) * '-')