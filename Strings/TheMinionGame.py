'''
Title     : The Minion Game
Subdomain : Strings
Domain    : Python
Author    : Arafat Hoshen
Created   : 10 October 2022
Problem   : https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
My YouTube: https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA
'''

def minion_game(s):
    s1=0
    s2=0
    vow='AEIOU'
    for i in range(len(s)):
        if s[i] not in vow:
            s1=s1+(len(s)-i)
        else:
            s2=s2+(len(s)-i)
    if s1>s2:
        print("Stuart",s1)
    elif s2>s1:
        print("Kevin",s2)
    else:
        print("Draw")