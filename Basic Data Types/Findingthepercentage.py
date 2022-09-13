"""
Title           : Finding the percentage
Domain          : Python
Subdomain       : Introduction
Author          : Arafat Hoshen
Created         : 14 September 2022
Problem         : https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
Visit My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    res = sum(student_marks[query_name]) / len(student_marks[name])
    print("{:.2f}".format(res))