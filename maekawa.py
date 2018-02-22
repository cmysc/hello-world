#!/usr/bin/python
# -*- coding: utf-8 -*-
# Maekawa algo 
# Xinyi Huang

import random
import math
from multiprocessing import Pool, Process, Queue, Pipe, Lock, Manager
import os
import multiprocessing
import formQuorum as ds

print ("hw start, Maekawa algorithm - sync---------- ")
'''
# pseudo
def sendingMessage(message, fromPi,toPj):
    while(toPj donot reply); # do nothing but keep looping and wait for reply
    return true; # if got replied return true
   
        


def receiveMessage(message, fromPi,toPj):
    if message =='request':
        if (toPj['state'] = HELD or toPj['voted'] = TRUE):
            Q.enqueue(fromPi)
        else
            sendingMessage('reply',fromPj, toPi)

'''

#-------- process pi function -------
def eachPi(x):  # d is a dict used for queue
    
    #initial state
    print x

    #change the state for all process
    x['state'] = random.choice(['WANTED','RELEASED'])
    print x['state']
    print os.getpid()
    # action after the state changes
    if (x['state'] == 'WANTED') :
        # Multicast request to all processes in Vi
        for member in x['voteSetForPi']:
            print member
            counter = 0 # to find how many in quorum replied
            for qv in Set:
                if qv['Pi'] == member:
                    print qv
                    '''
                    #?? how to get particular thread Pj which contain information qv as qvPj??? 
                    
                    # all become pseudo code below 
                    # set connection beweeen this two selfpi and qvPj
                    selfPi, qvPj = Pipe()
                   
                    # send the message 'request' through Pipe, and return bool true if replied
                    replied = sendingMessage('request',selfPi, qvPj)
                    
                    # receive the message
                    
                        
                    # count the number of VOTE, 
                    # if it is not equal to K 
                        # going to the waiting queue
                    # else 
                        # change qv's voted state  = HELD to enter 
                        #lock the critical section
                        # wait this qv finish sleep
                        # unlock the CS
                        # change qv's state = RELEASED
                        # wake up a Pi in the queue by sending message 'released'

                    ......     
                    '''
#----------------------
def worker(d, key):
    d[key] = key

#------------- main -----------------------
if __name__ == '__main__':   
    print ("---- part 1)---------- ")
    N =  random.randint(4,9)
    # get result from part 1) forming quorum 
    Set = []
    Set = ds.createNprocessVotingSet(N)
    print '\n'
    print Set


# ------------ part 2) ----------
    print ("---- part 2) ?? ---------- ")


    p = Pool(N)
    p.map(eachPi, Set)

    '''
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    p1 = multiprocessing.Process(target= eachPi, args=(d, Set[0]))
    jobs = [ multiprocessing.Process(target= eachPi, args=(d, Set[i]))
             for i in range(9) 
             ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print ('Results:' )
    
    
    '''

    


print ("hw end -----------")

