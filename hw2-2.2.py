#!/usr/bin/python
# -*- coding: utf-8 -*-
# min-max scheduling
# Xinyi Huang

print ('hw-start: min-max scheduling')


# ------------- helper function 1-------------

def findMinInListOfDic(templs,attr,attr1,attr2,attr3):
    ''' find the min number in temples list, according to attribute var attr '''

    #print 'templs:', templs
    seq = [d[attr] for d in templs if d[attr] is not 0]
    #print seq
    minValue = min(seq)
    #print minValue
    minResult = []
    for d in templs:
        if d[attr] == minValue:

            minResult.append({attr1: d[attr1], attr2: d[attr2],attr3: d[attr3]})

            # break;

    return minResult

# ------------- helper function 2-------------

def findMaxInListOfDic(templs,attr,attr1,attr2,attr3):
    ''' find the min number in temples list, according to attribute var attr '''

    #print 'templs:', templs
    seq = [d[attr] for d in templs if d[attr] is not 0]
   # print seq
    maxValue = max(seq)
    #print maxValue
    maxResult = []
    for d in templs:
        if d[attr] == maxValue:

            maxResult.append({attr1: d[attr1], attr2: d[attr2],attr3: d[attr3]})

            # break;

    return maxResult





# ---------------- find min Task On Machine --------------------------
def min_max_schedual(data):
    taskNum = data[0]['task']
    templs = []
    minTaskOnMachine = []


    for i in range(0, len(data)):

        if data[i]['task'] == str(taskNum):
            templs.append(data[i])
        elif data[i]['task'] != str(taskNum):

            # update taskNum case and add new data to templs
            tempRes = findMinInListOfDic(templs, 'timeCost', 'task', 'machine','timeCost')
            if len(tempRes) > 1:
                for x in tempRes:
                    minTaskOnMachine.append(x)
                   
            else:
                minTaskOnMachine.append(tempRes[0])
               
            # add new data to templs again
            templs = []
            templs.append(data[i])
            taskNum = data[i]['task']
         

        # find that min task name for the task == 7 case
        if i + 1 == len(data):
            tempRes = findMinInListOfDic(templs, 'timeCost', 'task', 'machine','timeCost')
            for x in tempRes:
                minTaskOnMachine.append(x)
    #endFor
               

    tempRes = findMaxInListOfDic(minTaskOnMachine, 'timeCost', 'task', 'machine', 'timeCost')
    finalMaxTaskOverAllMachines = []
    for x in tempRes:
        finalMaxTaskOverAllMachines.append(x)
    print 'Stage - MinMaxTask is assigned:'
    print finalMaxTaskOverAllMachines

    # -----------------  remove the min machine from data ---------------------
    dataRemoved = [d for d in data if d['task']not in [x['task'] for x in finalMaxTaskOverAllMachines]]
    #print '-----------'
    #print "dataRemoved len:"#,dataRemoved
    #print len(dataRemoved)
    if (len(dataRemoved) == 0):
        print "terminated"
        return
    else:

    # ----------------- update other task timeCost on the same min machine ---------------------

        dataUpdated = []
    
        for d in dataRemoved:
            # for the same machine
            if d['machine'] in [x['machine'] for x in finalMaxTaskOverAllMachines]:
                for x in finalMaxTaskOverAllMachines:
                    if x['machine'] == d['machine'] and d['timeCost']!=0:
                        d['timeCost'] = d['timeCost'] + x['timeCost']
                        dataUpdated.append({'task':d['task'], 'machine':d['machine'],'timeCost':d['timeCost']})
            # for different machine
            else:
                dataUpdated.append({'task':d['task'], 'machine':d['machine'],'timeCost':d['timeCost']})
        #print '-----------'
        #print "dataUpdated len:"#, dataUpdated 
        #print len(dataUpdated)
        print "==========recursive call ====="   
        #result = []
        #result.append(min_max_schedual(dataUpdated))
        min_max_schedual(dataUpdated)

###########################
# main function
def main():

    # ---------------data prepare------

    NaN = 0
    arr = [
        [
            0,
            13,
            79,
            23,
            71,
            60,
            27,
            2,
            ],
        [
            1,
            31,
            13,
            14,
            94,
            60,
            61,
            57,
            ],
        [
            2,
            17,
            1,
            NaN,
            23,
            36,
            8,
            86,
            ],
        [
            3,
            19,
            28,
            10,
            4,
            58,
            73,
            40,
            ],
        [
            4,
            94,
            75,
            NaN,
            58,
            NaN,
            68,
            46,
            ],
        [
            5,
            8,
            24,
            3,
            32,
            4,
            94,
            89,
            ],
        [
            6,
            10,
            57,
            13,
            1,
            92,
            75,
            29,
            ],
        [
            7,
            80,
            17,
            38,
            40,
            66,
            25,
            88,
            ],
        ]

    # print arr
    # print len(arr)

    Data = []
    for i in range(0, len(arr)):

        for j in range(0, len(arr[i])):

            if j != 0:
                tempData = {'task': str(i), 'machine': str(j - 1),
                            'timeCost': arr[i][j]}

                Data.append(tempData)

    # print data
    # print len(data)
    min_max_schedual(Data)

if __name__ == "__main__":
    main()

print 'hw-end'


			