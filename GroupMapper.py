import sys
import random
import math

def mainProgram(arg1, arg2):

    #Data Assign------------------------------------------------------------------

    topicList = []
    memberList = []
    groupList = {}
    counterDone = 0
    groupNum = 1

    topicFile  = open(arg1, "r") 
    contents = topicFile.readlines()
    for line in contents:
        topicList.append(line)
    topicFile.close()

    memberFile  = open(arg2, "r") 
    contents = memberFile.readlines()
    for line in contents:
        memberList.append(line)
    memberFile.close()


    #Algorithm Core--------------------------------------------------------------
    minNumberMembers = len(memberList)//len(topicList)
    if type(minNumberMembers) == float:
        minNumberMembers = math.modf(minNumberMembers) 
        
    for selectorV in topicList:
        groupList[selectorV] = []

    while counterDone < len(topicList):
        for target_list in groupList.values():
            if len(target_list) < minNumberMembers:
                for selectorV in topicList:
                    groupList[selectorV] = []
                newIndex = random.randrange(0, len(topicList))
                for selectorV in memberList:
                    groupList[topicList[newIndex]].append(selectorV)
                    oldIndex = newIndex
                    while oldIndex == newIndex:
                        newIndex = random.randrange(0, len(topicList))   
                counterDone = 0
            else:
                counterDone += 1

    #Results-----------------------------------------------------------------------
    for groupItem in groupList.items():
        print("Asunto: " + groupItem[0]) 
        print("Grupo %d:" %groupNum)
        for valuesItem in groupItem[1]:
            print(" --  " + valuesItem)
        groupNum += 1    


if __name__== "__main__":
    mainProgram(str(sys.argv[1]), str(sys.argv[2]))
