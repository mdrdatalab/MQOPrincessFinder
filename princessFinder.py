# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 13:40:02 2017

@author: michael
"""

import random


def dist1(guess, point):
    z1 = -(point[0]+point[1])
    z2= -(guess[0]+guess[1])
    return max((abs(point[0]-guess[0])),abs(point[1]-guess[1]),abs(z1-z2))
    

def possibilities(loc, distance, feasibleSet):
    #need to double check logic of distmax and distmin... something isn't working
    if distance < 0:
        temp = []
        for x in feasibleSet:
            if (dist1(x,loc) < 100):
                temp.append(x)
        return list(set(feasibleSet) - set(temp))
        
    distmax = distance
    distmin = distances[distances.index(distance)+1]
    temp = []
    if feasibleSet == []:
        for x in range(1000):
            for y in range(1000):
                dist = dist1(loc,(x,y))
                if (dist <= distmax) and (dist > distmin):
                    feasibleSet.append((x,y))
    
        
    for x in feasibleSet:
        if (dist1(x, loc) <= distmax) and (dist1(x, loc) > distmin):
            temp.append(x)                    
                     
    
    return list(temp)

if __name__ == "__main__":        
    feasibleSet = []
    distances = [100,25,10,5,0, 0]
    
    d = 999
    while d!=0:
        print("Looking for princess... Enter 0 distance to exit")
        print("Size of feasible set %s tiles" %(len(feasibleSet)))
        try:
            rcoords = input("Enter coordinates separated by a comma: ")
            coords = rcoords.replace(" ","").split(",")
            coords = (int(coords[0]),int(coords[1]))
            d = int(input("Enter distance (0 to exit): "))
            feasibleSet = possibilities(coords, d, feasibleSet)
        except Exception:
            input("Invaid input")
    input("Princess Found! \nTerminating script")
            
