'''
Title     : Merge the Tools
Subdomain : Strings
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
'''

def merge_the_tools(string, k):
    l=[]
    m=0
    for i in range(len(string)//k):
        l.append(string[m:m+k])
        m+=k
    for v in l:
        print(''.join(list(dict.fromkeys(list(v)).keys())))