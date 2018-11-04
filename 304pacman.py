#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

END = False

def find(tab, char) :
    pos = [0, 0]
    for line in tab :
        for elt in line :
            if (elt == char) :
                return pos
            pos[1] +=1
        pos[0] +=1
        pos[1] = 0

def checkend(tab, pos) :
    if (tab[pos[0] - 1][pos[1]] == 'P' or tab[pos[0]][pos[1] + 1] == 'P' or tab[pos[0] + 1][pos[1]] == 'P' or tab[pos[0]][pos[1] - 1] == 'P') :
        for line in tab :
            for elt in line :
                print(elt, end='')
            print()
        exit()


def evalnear(tab, pos, empty, weight, branch) :
    checkend(tab, pos)
    if (tab[pos[0] - 1][pos[1]] == empty) :
        tab[pos[0] - 1][pos[1]] = (weight % 10)
        branch.append([[pos[0] - 1, pos[1]], []])
    if (tab[pos[0]][pos[1] + 1] == empty) :
        tab[pos[0]][pos[1] + 1] = (weight % 10)
        branch.append([[pos[0], pos[1] + 1], []])
    if (tab[pos[0] + 1][pos[1]] == empty) :
        tab[pos[0] + 1][pos[1]] = (weight % 10)
        branch.append([[pos[0] + 1, pos[1]], []])
    if (tab[pos[0]][pos[1] - 1] == empty) :
        tab[pos[0]][pos[1] - 1] = (weight % 10)
        branch.append([[pos[0], pos[1] - 1], []])


def endbranch(tab, weight, branch, empty, turn) :

    if (weight > 0) :
        for item in branch[1] :
            endbranch(tab, weight -1, item, empty, turn)
    evalnear(tab, branch[0], empty, turn + 1, branch[1])

def algo(tab, wall, empty) :
    weight = 0
    allbranch = []
    allbranch.append(find(tab, 'F'))
    allbranch.append([])
    global END

    while (END == False) :
        endbranch(tab, weight, allbranch, empty, weight)
        weight += 1


def main() :
    if (len(sys.argv) == 4) :
        wall = sys.argv[2]
        empty = sys.argv[3]
        file = open(sys.argv[1], "r")
        lines = file.read().rstrip()
        tab = lines.split('\n')
        if (len(tab) <= 1) :
            return 84
        newtab = []
        for i in range(0, len(tab)) :
            str = []
            for j in range(0, len(tab[i])) :
                if tab[i][j] == '1' :
                    str.append(wall)
                elif tab[i][j] == '0' :
                    str.append(empty)
                else :
                    str.append(tab[i][j])
            newtab.append(str)
        algo(newtab, wall, empty)
    else :
        return (84);

#try :
if (main() == 84) :
    exit(84)
#except :
    #exit(84)
