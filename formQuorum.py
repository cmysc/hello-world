#!/usr/bin/python
# -*- coding: utf-8 -*-
# Maekawa algo 
# Xinyi Huang
import random
import math

print ("hw start, Maekawa algorithm - form Quorum---------- ")

#-------------- helper function ----------------
def squareRootFloor(n):
    if n<1:
        return False
    else:
        temp = 0
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return i
            elif i*i< n:
                temp = i
        return temp

    
def getColumnElement(matr,j):
    ''' get column j element in matr '''
    e_in_colj = []
    for i in range(0,len(matr)):
        e_in_colj.append(matr[i][j])
    #print 'e_in_colj',e_in_colj
    return e_in_colj
    

#------------- part 1) tested by random L -----------------
def createNprocessVotingSet(N):
    
   
    print "random between (4,9) for N = ",N
    
    L = squareRootFloor(N)
    print "matrix length floor is ",L
    
    MissNumElem = 0
    if int(math.pow(L,2))== N:
        K = 2*L-1
    else:
        L = L + 1
        K = 2*(L)-1
        MissNumElem = int(math.pow(L,2)) - N
        print "need grab", MissNumElem , "existing elements to extend the size of matrix as",int(math.pow(L,2))
    print "L = ",L   
    print "K = ",K

    #processor set
    print '--- the pi set is the following -----'
    pSet = [x for x in range(1,N+1)]
    newAppend = MissNumElem
    while MissNumElem != 0:
        pSet.append(newAppend - MissNumElem +1)
        MissNumElem -=1
    print "pSet=",pSet

    #initalize arr
    pMatr =[[0 for x in range(0,L)] for x in range(0,L)]
    
    pointer = 0
    for i in range(0,L):
        for j in range(0,L):       
            pMatr[i][j] = pSet[pointer]
            pointer += 1

    print pMatr


    #--------- method2 to determine the voting set si, initialization included ----------
    S = []
    counter = 0
    for i in range(0,L):
        for j in range(0,L):
            counter += 1
            pi = pMatr[i][j]
            tmpSet = []
        
            for x in pMatr[i]:
                tmpSet.append(x)
            for x in getColumnElement(pMatr,j):
                tmpSet.append(x)

            voteSet = list(set(tmpSet))
            si = {'voteSetName':'V'+str(pi),"voteSetForPi":voteSet,'Pi':counter,'state': 'RELEASED','voted': 'FALSE'}
            S.append(si)
    print '--- the voting set for each pi determined by method2 is the following -----'
    # initialzation included
    for x in S:
        print x
    return S

#------------- main -----------------------
if __name__ == '__main__':   
    print ("---- part 1) form quorum set ---------- ")
    n =  random.randint(4,9)
    Set = []
    Set = createNprocessVotingSet(n)
    #print Set

    

# ------------ part 3) ----------

an3 = '''There will be a deadlock if a kind of waiting cycle exist as the following:
        p1 is waiting for v1 to give the permission, but v1 give it to p2 which is also in v1, 
        p2 is waiting for v2 to give the permission, but v2 give it to p3 which is also in v2, 
        p3 is waiting for v3 to give the permission, but v3 give it to p4 which is also in v3, 
        ...
        pN is waiting for vN to give the permission, but vN give it to p1 which is also in vN

        However, since the set of all processes can be uniquely ordered by timestamp of request, 
        there must be a node whose request's timestamp is preceded by those of both of its adjacent nodes.
        After removing this preceded node, the cycle can be broken. 
        
        So, deadlock is not possible.
        
        '''
print '---- part 3) ------\n', an3

print ("hw end -----------")

