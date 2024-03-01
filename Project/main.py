# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame as p

s1=[]
s1.append(input('ENTER YOUR NAME PLAYER 1'))
s1.append(input('ENTER YOUR NAME PLAYER 2'))
W = [0]
B = [0]

p.init()
h = w = 512
s = p.display.set_mode((512, 512))
p.display.set_caption("M-S-T's ChessEngine")
l=p.image.load('chess-board.png')
p.display.set_icon(l)
c = [p.Color('white'), p.Color('grey')]
sq = h//8
pi = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wK', 'wB', 'wQ', 'wN', 'wP']
b_board = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
           ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
           ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
           ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
           ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR']]
pics = {}
for i in pi:
    pics[i] = p.transform.scale(p.image.load(i+'.png'), (64, 64))


def chess_board():
    for i in range(8):
        for j in range(8):
            c1 = c[(i+j) % 2]
            p.draw.rect(s, c1, p.Rect(j*sq, i*sq, sq, sq))

    for i in range(8):
        for j in range(8):
            if b_board[i][j] != '  ':
                s.blit(pics[b_board[i][j]], p.Rect(j*sq, i*sq, 64, 64))
f = 1
prev = [-1, -1]


def validation(a, b):
    m = b_board[a[0]][a[1]]
    if m[0] == 'b':
        if m[1] == 'P':
            if a[0] == 1 and b[0] == 3 and a[1] == b[1] and b_board[a[0]+1][a[1]] == '  ' and b_board[b[0]][b[1]] == '  ':
                return 1
            elif a[0]+1 == b[0] and a[1] == b[1] and b_board[b[0]][b[1]] == '  ':
                return 1
            elif a[0]+1 == b[0] and (a[1]+1 == b[1] or a[1]-1 == b[1]) and b_board[b[0]][b[1]][0] == 'w':
                if b_board[b[0]][b[1]][1] == 'K':
                    return 22
                return 11
            return 0


        elif m[1] == 'R':
            if a[0] == b[0] or a[1] == b[1]:
                f=0
                c=[0,0,0,0]
                while a[1]!=b[1] or a[0]!=b[0]:
                    if a[0]+(c[0]+1)<b[0] and b_board[a[0]+(c[0]+1)][a[1]]=='  ' and b_board[a[0]+(c[0]+1)][a[1]][0]!='b' and (f==0 or f==1):
                        c[0]+= 1
                        f = 1
                    elif a[0]+(c[1]-1)>b[0] and b_board[a[0]+(c[1]-1)][a[1]]=='  ' and b_board[a[0]+(c[1]-1)][a[1]][0]!='b' and (f==0 or f==2):
                        f = 2
                        c[1]-=1
                    elif a[1]+(c[2]+1)<b[1] and b_board[a[0]][a[1]+(c[2]+1)]=='  ' and b_board[a[0]][a[1]+(c[2]+1)][0]!='b' and (f==0 or f==3):
                        f = 3
                        c[2]+=1
                    elif a[1]+(c[3]-1)>b[1] and b_board[a[0]][a[1]+(c[3]-1)]=='  ' and b_board[a[0]][a[1]+(c[3]-1)][0]!='b' and (f==0 or f==4):
                        f = 4
                        c[3]-=1
                    else:
                        if f<=2 and (a[0]+(c[f-1]+1)==b[0] or a[0]+(c[f-1]-1)==b[0]) and a[1]==b[1]:
                            if b_board[b[0]][b[1]] == 'wK':
                                return 22
                            elif b_board[b[0]][b[1]][0] == 'w':
                                return 11
                            elif b_board[b[0]][b[1]]=='  ':
                                return 1
                        elif f>2 and a[0]==b[0] and (a[1]+(c[f-1]+1)==b[1] or a[1]+(c[f-1]-1) == b[1]):
                            if b_board[b[0]][b[1]] == 'wK':
                                return 22
                            elif b_board[b[0]][b[1]][0] == 'w':
                                return 11
                            elif b_board[b[0]][b[1]] == '  ':
                                return 1
                        else:
                            if abs(a[0]-b[0])==1 or abs(a[1]-b[1])==1:
                                if b_board[b[0]][b[1]] == 'wK':
                                    return 22
                                elif b_board[b[0]][b[1]][0] == 'w':
                                    return 11
                                elif b_board[b[0]][b[1]] == '  ':
                                    return 1
                        return 0
                return 0

        elif m[1]=='N':
            d1 = a[0]-b[0]
            d2 = a[1]-b[1]
            if (d1==1 and d2==2) or (d1==2 and d2==1) or (d1==-2 and d2==1) or (d1==2 and d2==-1) or (d1==-1 and d2==-2) or (d1==-2 and d2==-1) or (d1==-1 and d2==2) or (d1==1 and d2==-2):
                if b_board[b[0]][b[1]]=='  ':
                    return 1
                elif b_board[b[0]][b[1]]=='wK':
                    return 22
                elif b_board[b[0]][b[1]][0]=='w':
                    return 11
            return 0

        elif m[1]=='B':
            d1 = (b[0]-a[0])
            d2 = (b[1]-a[1])
            c=0
            f=0
            while (abs(d1)==abs(d2))!=0:
                if abs(d1)==abs(d2) and c<abs(d1) and d1>0 and d2>0 and b_board[a[0]+(c+1)][a[1]+(c+1)]=='  ' and (f==0 or f==1):
                    c+=1
                    f=1
                elif abs(d1)==abs(d2) and c<abs(d1) and d1<0 and d2>0 and b_board[a[0]-(c+1)][a[1]+(c+1)]=='  ' and (f==0 or f==2):
                    c+=1
                    f=2
                elif abs(d1)==abs(d2) and c<abs(d1) and d1>0 and d2<0 and b_board[a[0]+(c+1)][a[1]-(c+1)]=='  ' and (f==0 or f==3):
                    c+=1
                    f=3
                elif abs(d1)==abs(d2) and c<abs(d1) and d1<0 and d2<0 and b_board[a[0]-(c+1)][a[1]-(c+1)]=='  ' and (f==0 or f==4):
                    c+=1
                    f=4
                elif abs(d1)==1:
                    if b_board[b[0]][b[1]]=='  ':
                        return 1
                    elif b_board[b[0]][b[1]]=='wK':
                        return 22
                    elif b_board[b[0]][b[1]][0]=='w':
                        return 11
                    else:
                        return 0
                else:
                    break
            if f>0:
                if b_board[b[0]][b[1]] == '  ':
                    return 1
                elif b_board[b[0]][b[1]] == 'wK':
                    return 22
                elif b_board[b[0]][b[1]][0] == 'w':
                    return 11
            return 0


        if m[1]=='Q':
            d1=(b[0]-a[0])
            d2=(b[1]-a[1])
            if abs(d1)==abs(d2):
                c = 0
                f = 0
                while (abs(d1) == abs(d2)) != 0:
                    if abs(d1) == abs(d2) and c < abs(d1) and d1 > 0 and d2 > 0 and b_board[a[0] + (c + 1)][a[1] + (c + 1)] == '  ' and (f == 0 or f == 1):
                        c += 1
                        print(a, b, c)
                        f = 1
                    elif abs(d1) == abs(d2) and c < abs(d1) and d1 < 0 and d2 > 0 and b_board[a[0] - (c + 1)][
                        a[1] + (c + 1)] == '  ' and (f == 0 or f == 2):
                        c += 1
                        f = 2
                    elif abs(d1) == abs(d2) and c < abs(d1) and d1 > 0 and d2 < 0 and b_board[a[0] + (c + 1)][
                        a[1] - (c + 1)] == '  ' and (f == 0 or f == 3):
                        c += 1
                        f = 3
                    elif abs(d1) == abs(d2) and c < abs(d1) and d1 < 0 and d2 < 0 and b_board[a[0] - (c + 1)][
                        a[1] - (c + 1)] == '  ' and (f == 0 or f == 4):
                        c += 1
                        f = 4
                    elif abs(d1) == 1:
                        if b_board[b[0]][b[1]] == '  ':
                            return 1
                        elif b_board[b[0]][b[1]] == 'wK':
                            return 22
                        elif b_board[b[0]][b[1]][0] == 'w':
                            return 11
                        else:
                            return 0
                    else:
                        break
                if f > 0:
                    if b_board[b[0]][b[1]] == '  ':
                        return 1
                    elif b_board[b[0]][b[1]] == 'wK':
                        return 22
                    elif b_board[b[0]][b[1]][0] == 'w':
                        return 11
            elif d1==0 or d2==0:
                f = 0
                c = [0, 0, 0, 0]
                while a[1] != b[1] or a[0] != b[0]:
                    if a[0] + (c[0] + 1) < b[0] and b_board[a[0] + (c[0] + 1)][a[1]] == '  ' and \
                            b_board[a[0] + (c[0] + 1)][a[1]][0] != 'b' and (f == 0 or f == 1):
                        c[0] += 1
                        f = 1
                    elif a[0] + (c[1] - 1) > b[0] and b_board[a[0] + (c[1] - 1)][a[1]] == '  ' and \
                            b_board[a[0] + (c[1] - 1)][a[1]][0] != 'b' and (f == 0 or f == 2):
                        f = 2
                        c[1] -= 1
                    elif a[1] + (c[2] + 1) < b[1] and b_board[a[0]][a[1] + (c[2] + 1)] == '  ' and \
                            b_board[a[0]][a[1] + (c[2] + 1)][0] != 'b' and (f == 0 or f == 3):
                        f = 3
                        c[2] += 1
                    elif a[1] + (c[3] - 1) > b[1] and b_board[a[0]][a[1] + (c[3] - 1)] == '  ' and \
                            b_board[a[0]][a[1] + (c[3] - 1)][0] != 'b' and (f == 0 or f == 4):
                        f = 4
                        c[3] -= 1
                    else:
                        if f <= 2 and (a[0] + (c[f - 1] + 1) == b[0] or a[0] + (c[f - 1] - 1) == b[0]) and a[1] == b[1]:
                            if b_board[b[0]][b[1]] == 'wK':
                                return 22
                            elif b_board[b[0]][b[1]][0] == 'w':
                                return 11
                            elif b_board[b[0]][b[1]] == '  ':
                                return 1
                        elif f > 2 and a[0] == b[0] and (
                                a[1] + (c[f - 1] + 1) == b[1] or a[1] + (c[f - 1] - 1) == b[1]):
                            if b_board[b[0]][b[1]] == 'wK':
                                return 22
                            elif b_board[b[0]][b[1]][0] == 'w':
                                return 11
                            elif b_board[b[0]][b[1]] == '  ':
                                return 1
                        else:
                            if abs(a[0] - b[0]) == 1 or abs(a[1] - b[1]) == 1:
                                if b_board[b[0]][b[1]] == 'wK':
                                    return 22
                                elif b_board[b[0]][b[1]][0] == 'w':
                                    return 11
                                elif b_board[b[0]][b[1]] == '  ':
                                    return 1
                        return 0
                return 0

        elif m[1]=='K':
            d1=a[0]-b[0]
            d2=a[1]-b[1]
            if (abs(d1)<2 and abs(d2)<2) and (a[0]!=b[0] or a[1]!=b[1]):
                if b_board[b[0]][b[1]]=='wK':
                    return 22
                elif b_board[b[0]][b[1]][0]=='w':
                    return 11
                elif b_board[b[0]][b[1]]=='  ':
                    return 1
            return 0


    if m[0]=='w':
        if m[1]=='P':
            if a[0]==6 and b[0]==4 and a[1]==b[1] and b_board[a[0]-1][a[1]]=='  ' and b_board[b[0]][b[1]]=='  ':
                return 1
            elif a[0]-1==b[0] and a[1]==b[1] and b_board[b[0]][b[1]]=='  ':
                return 1
            elif a[0]-1==b[0] and (a[1]-1==b[1] or a[1]+1==b[1]) and b_board[b[0]][b[1]][0]=='b':
                if b_board[b[0]][b[1]][1]=='K':
                    return 22
                return 11
            return 0


        elif m[1] == 'R':
            if a[0] == b[0] or a[1] == b[1]:
                f=0
                c=[0,0,0,0]
                while a[1]!=b[1] or a[0]!=b[0]:
                    if a[0]+(c[0]+1)<b[0] and b_board[a[0]+(c[0]+1)][a[1]]=='  ' and b_board[a[0]+(c[0]+1)][a[1]][0]!='w' and (f==0 or f==1):
                        c[0]+= 1
                        f = 1
                    elif a[0]+(c[1]-1)>b[0] and b_board[a[0]+(c[1]-1)][a[1]]=='  ' and b_board[a[0]+(c[1]-1)][a[1]][0]!='w' and (f==0 or f==2):
                        f = 2
                        c[1]-=1
                    elif a[1]+(c[2]+1)<b[1] and b_board[a[0]][a[1]+(c[2]+1)]=='  ' and b_board[a[0]][a[1]+(c[2]+1)][0]!='w' and (f==0 or f==3):
                        f = 3
                        c[2]+=1
                    elif a[1]+(c[3]-1)>b[1] and b_board[a[0]][a[1]+(c[3]-1)]=='  ' and b_board[a[0]][a[1]+(c[3]-1)][0]!='w' and (f==0 or f==4):
                        f = 4
                        c[3]-=1
                    else:
                        if f<=2 and (a[0]+(c[f-1]+1)==b[0] or a[0]+(c[f-1]-1)==b[0]) and a[1]==b[1]:
                            if b_board[b[0]][b[1]] == 'bK':
                                return 22
                            elif b_board[b[0]][b[1]][0] == 'b':
                                return 11
                            elif b_board[b[0]][b[1]]=='  ':
                                return 1
                        elif f>2 and a[0]==b[0] and (a[1]+(c[f-1]+1)==b[1] or a[1]+(c[f-1]-1) == b[1]):
                            if b_board[b[0]][b[1]] == 'bK':
                                return 22
                            elif b_board[b[0]][b[1]][0] == 'w':
                                return 11
                            elif b_board[b[0]][b[1]] == '  ':
                                return 1
                        else:
                            if abs(a[0]-b[0])==1 or abs(a[1]-b[1])==1:
                                if b_board[b[0]][b[1]] == 'bK':
                                    return 22
                                elif b_board[b[0]][b[1]][0] == 'b':
                                    return 11
                                elif b_board[b[0]][b[1]] == '  ':
                                    return 1
                        return 0
                return 0



        elif m[1]=='N':
            d1 = a[0]-b[0]
            d2 = a[1]-b[1]
            if (d1==1 and d2==2) or (d1==2 and d2==1) or (d1==-2 and d2==1) or (d1==2 and d2==-1) or (d1==-1 and d2==-2) or (d1==-2 and d2==-1) or (d1==-1 and d2==2) or (d1==1 and d2==-2):
                if b_board[b[0]][b[1]]=='  ':
                    return 1
                elif b_board[b[0]][b[1]]=='wK':
                    return 22
                elif b_board[b[0]][b[1]][0]=='w':
                    return 11
            return 0


        elif m[1]=='B':
            d1 = (b[0]-a[0])
            d2 = (b[1]-a[1])
            c=0
            f=0
            while (abs(d1)==abs(d2))!=0:
                if abs(d1)==abs(d2) and c<abs(d1) and d1>0 and d2>0 and b_board[a[0]+(c+1)][a[1]+(c+1)]=='  ' and (f==0 or f==1):
                    c+=1
                    print(a,b,c)
                    f=1
                elif abs(d1)==abs(d2) and c<abs(d1) and d1<0 and d2>0 and b_board[a[0]-(c+1)][a[1]+(c+1)]=='  ' and (f==0 or f==2):
                    c+=1
                    f=2
                elif abs(d1)==abs(d2) and c<abs(d1) and d1>0 and d2<0 and b_board[a[0]+(c+1)][a[1]-(c+1)]=='  ' and (f==0 or f==3):
                    c+=1
                    f=3
                elif abs(d1)==abs(d2) and c<abs(d1) and d1<0 and d2<0 and b_board[a[0]-(c+1)][a[1]-(c+1)]=='  ' and (f==0 or f==4):
                    c+=1
                    f=4
                elif abs(d1)==1:
                    if b_board[b[0]][b[1]]=='  ':
                        return 1
                    elif b_board[b[0]][b[1]]=='bK':
                        return 22
                    elif b_board[b[0]][b[1]][0]=='b':
                        return 11
                    else:
                        return 0
                else:
                    break
            if f>0:
                if b_board[b[0]][b[1]] == '  ':
                    return 1
                elif b_board[b[0]][b[1]] == 'bK':
                    return 22
                elif b_board[b[0]][b[1]][0] == 'b':
                    return 11

            return 0

        elif m[1]=='Q':
            d1 = (b[0] - a[0])
            d2 = (b[1] - a[1])
            if abs(d1) == abs(d2):
                c = 0
                f = 0
                while (abs(d1) == abs(d2)) != 0:
                    if abs(d1) == abs(d2) and c < abs(d1) and d1 > 0 and d2 > 0 and b_board[a[0] + (c + 1)][
                        a[1] + (c + 1)] == '  ' and (f == 0 or f == 1):
                        c += 1
                        print(a, b, c)
                        f = 1
                    elif abs(d1) == abs(d2) and c < abs(d1) and d1 < 0 and d2 > 0 and b_board[a[0] - (c + 1)][
                        a[1] + (c + 1)] == '  ' and (f == 0 or f == 2):
                        c += 1
                        f = 2
                    elif abs(d1) == abs(d2) and c < abs(d1) and d1 > 0 and d2 < 0 and b_board[a[0] + (c + 1)][
                        a[1] - (c + 1)] == '  ' and (f == 0 or f == 3):
                        c += 1
                        f = 3
                    elif abs(d1) == abs(d2) and c < abs(d1) and d1 < 0 and d2 < 0 and b_board[a[0] - (c + 1)][
                        a[1] - (c + 1)] == '  ' and (f == 0 or f == 4):
                        c += 1
                        f = 4
                    elif abs(d1) == 1:
                        if b_board[b[0]][b[1]] == '  ':
                            return 1
                        elif b_board[b[0]][b[1]] == 'bK':
                            return 22
                        elif b_board[b[0]][b[1]][0] == 'b':
                            return 11
                        else:
                            return 0
                    else:
                        break
                if f > 0:
                    if b_board[b[0]][b[1]] == '  ':
                        return 1
                    elif b_board[b[0]][b[1]] == 'bK':
                        return 22
                    elif b_board[b[0]][b[1]][0] == 'b':
                        return 11
            if a[0] == b[0] or a[1] == b[1]:
                f=0
                c=[0,0,0,0]
                while a[1]!=b[1] or a[0]!=b[0]:
                    if a[0]+(c[0]+1)<b[0] and b_board[a[0]+(c[0]+1)][a[1]]=='  ' and b_board[a[0]+(c[0]+1)][a[1]][0]!='w' and (f==0 or f==1):
                        c[0]+= 1
                        f = 1
                    elif a[0]+(c[1]-1)>b[0] and b_board[a[0]+(c[1]-1)][a[1]]=='  ' and b_board[a[0]+(c[1]-1)][a[1]][0]!='w' and (f==0 or f==2):
                        f = 2
                        c[1]-=1
                    elif a[1]+(c[2]+1)<b[1] and b_board[a[0]][a[1]+(c[2]+1)]=='  ' and b_board[a[0]][a[1]+(c[2]+1)][0]!='w' and (f==0 or f==3):
                        f = 3
                        c[2]+=1
                    elif a[1]+(c[3]-1)>b[1] and b_board[a[0]][a[1]+(c[3]-1)]=='  ' and b_board[a[0]][a[1]+(c[3]-1)][0]!='w' and (f==0 or f==4):
                        f = 4
                        c[3]-=1
                    else:
                        if f<=2 and (a[0]+(c[f-1]+1)==b[0] or a[0]+(c[f-1]-1)==b[0]) and a[1]==b[1]:
                            print(1)
                            if b_board[b[0]][b[1]] == 'bK':
                                return 22
                            elif b_board[b[0]][b[1]][0] == 'b':
                                return 11
                            elif b_board[b[0]][b[1]]=='  ':
                                return 1
                        elif f>2 and a[0]==b[0] and (a[1]+(c[f-1]+1)==b[1] or a[1]+(c[f-1]-1) == b[1]):
                            print(2)
                            if b_board[b[0]][b[1]] == 'bK':
                                return 22
                            elif b_board[b[0]][b[1]][0] == 'w':
                                return 11
                            elif b_board[b[0]][b[1]] == '  ':
                                return 1
                        else:
                            if abs(a[0]-b[0])==1 or abs(a[1]-b[1])==1:
                                if b_board[b[0]][b[1]] == 'bK':
                                    return 22
                                elif b_board[b[0]][b[1]][0] == 'b':
                                    return 11
                                elif b_board[b[0]][b[1]] == '  ':
                                    return 1
                        return 0
                print(a,b,c,f)
                return 0

        elif m[1]=='K':
            d1=a[0]-b[0]
            d2=a[1]-b[1]
            if (abs(d1)<2 and abs(d2)<2) and (a[0]!=b[0] or a[1]!=b[1]):
                print('king w',1)
                if b_board[b[0]][b[1]]=='bK':
                    return 22
                elif b_board[b[0]][b[1]][0]=='b':
                    return 11
                elif b_board[b[0]][b[1]]=='  ':
                    return 1
            return 0
    return 0




def Prob_to_win():
    print()
    print()
    if W[0] > B[0]:
        print('Looks like game winning is favourable to ' + s1[0])
    elif W[0] < B[0]:
        print('Looks like game winning is favourable to ' + s1[1])
    else:
        print('Looks like game id going to be tie')
    print()
    print()
    print()

print(s1[0] + ' turn (whites)')
while f:
    if f==1:
        for e in p.event.get():
            if e.type == p.QUIT:
                f = 0
            elif e.type == p.MOUSEBUTTONDOWN:
                loc = p.mouse.get_pos()
                y=loc[0]//64
                x=loc[1]//64

                if [x, y]!=prev and prev != [-1, -1] and b_board[prev[0]][prev[1]][0]=='w':
                    v=validation(prev,[x, y])
                    if v==1:
                        t=b_board[x][y]
                        b_board[x][y]=b_board[prev[0]][prev[1]]
                        b_board[prev[0]][prev[1]]=t
                        print(b_board[x][y]+' made a safe move')
                        prev = [-1, -1]
                        f=2
                        v=-1
                        Prob_to_win()
                        print(s1[1]+' turn (blacks)')
                    elif [x, y] != prev and prev != [-1, -1] and v>=11:
                        if v==11:
                            print(b_board[prev[0]][prev[1]]+' killed '+b_board[x][y])
                            b_board[x][y]=b_board[prev[0]][prev[1]]
                            b_board[prev[0]][prev[1]]='  '
                            f=2
                            prev = [-1, -1]
                            v=-1
                            W[0]+=1
                            Prob_to_win()
                            print(s1[1]+' turn (blacks)')
                        else:
                            print(s1[0]+' wins')
                            f=0
                    elif v==0:
                        prev=[-1,-1]
                elif [x, y]!=prev and prev == [-1, -1] and b_board[x][y][0]=='w':
                    print(s1[0]+' picked '+b_board[x][y])
                    prev[0] = x
                    prev[1] = y
                else:
                    prev=[-1,-1]
                    print('Wrong move')
    chess_board()
    p.display.flip()

    if f==2:
        for e in p.event.get():
            if e.type == p.QUIT:
                f = 0
            elif e.type == p.MOUSEBUTTONDOWN:
                loc = p.mouse.get_pos()
                y=loc[0]//64
                x=loc[1]//64

                if [x, y]!=prev and prev != [-1, -1] and b_board[prev[0]][prev[1]][0]=='b':
                    v=validation(prev,[x, y])
                    if v==1:
                        t=b_board[x][y]
                        b_board[x][y]=b_board[prev[0]][prev[1]]
                        b_board[prev[0]][prev[1]]=t
                        print(b_board[x][y]+' made a safe move')
                        prev = [-1, -1]
                        f=1
                        v=-1
                        Prob_to_win()
                        print(s1[0]+' turn (whites)')

                    elif [x, y] != prev and prev != [-1, -1] and v >= 11:
                        if v == 11:
                            print(b_board[prev[0]][prev[1]]+' killed '+b_board[x][y])
                            b_board[x][y] = b_board[prev[0]][prev[1]]
                            b_board[prev[0]][prev[1]] = '  '
                            f = 1
                            prev = [-1, -1]
                            v=-1
                            B[0]+=1
                            Prob_to_win()
                            print(s1[0]+' turn (whites)')
                        else:
                            print(s1[1]+' wins')
                            f = 0
                    elif v==0:
                        prev=[-1,-1]
                elif [x, y]!=prev and prev == [-1, -1] and b_board[x][y][0]=='b':
                    print(s1[1]+' picked '+b_board[x][y])
                    prev[0] = x
                    prev[1] = y
                else:
                    prev=[-1,-1]
                    print('wrong move')
    chess_board()
    p.display.flip()






