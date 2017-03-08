# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 01:01:21 2017

@author: michael
"""

import random

def dist1(guess, point):
    z1 = -(point[0]+point[1])
    z2= -(guess[0]+guess[1])
    return max((abs(point[0]-guess[0])),abs(point[1]-guess[1]),abs(z1-z2))  
    
def makeGuess(loc):
    distance = dist1(loc, princess)
    if distance == 0:
        print("You have found the princess!")
        d = 0
    elif distance <= 5:
        print("The princess is within 5 squares!")
        d = 5
    elif distance <= 10:
        print("The princess is within 10 squares!")
        d = 10
    elif distance <= 25:
        print("The princess is within 25 squares!")
        d = 25
    elif distance <= 100:
        print("The princess is within 100 squares")
        d = 100
    else:
        print("The princess is not within 100 squares")
        d = -100
        
    return d
    
    
def valid_moves(loc):
    moves = []
    dy_max = 7
    x_start = -5
    for y in range(-dy_max,dy_max+1):
        if y%2 == 1:
            x_span = 18
        else:
            x_span = 19
            x_start -= 1
        for x in range(x_span):
            moves.append((loc[0]+x_start+x,loc[1]+y))
    return moves
        
def move(loc, target):
    dist = dist1(loc, target)
    cost = 2 + 0.9*dist
    return target, -cost
    
def search(loc):
    reward = -5
    clue = makeGuess(loc)
    return clue, reward
    


    
def interactive(loc, clue, reward):
    moves = valid_moves(loc)
    #show index of right, left, up, down, current
    target = int(input("Enter move: "))
    pos = moves[target]
    return pos
    

    
    
def runSearch(policy, seed=None, start = None):
    random.seed(seed)
    global princess
    reward = 0
    step = 0
    clue = None
    princess = [random.randrange(0,1000),random.randrange(0,1000)]
    if start != None:
        loc = start
    else:
        loc = [random.randrange(0,1000),random.randrange(0,1000)]
        
    history = [(step, loc, "start", clue, reward)]    
    print(history[-1])
    while True:
        step+= 1
        act = policy(loc, clue, reward)
        #policy returns a location, if it is the current, search, else move
        if act == loc:
            clue, r = search(loc)
            reward += r
            history.append((step, loc, "search", clue, reward))
            if clue == 0:
                break
        if act != loc:
            loc, r = move(loc, act)
            reward += r
            clue = None
            history.append((step, loc, "move", clue, reward))
        print(history[-1])
        
        
        