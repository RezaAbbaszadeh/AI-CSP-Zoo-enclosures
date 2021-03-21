import sys
import copy
from time import time

def CSP(assignment, values, index, i , arc):
    #remove this animal from other cages
    for n in range(cage_count):
        if values[index][i] in values[n] and index!=n:
            values[n].remove(values[index][i])
            if len(values[n])==0:
                return False

    #remove bad animals from neighbor cages
    index+=1
    for j in adjacents:
        if index in j:
            x = j[0]  # cage[index] is adjacent with cage[x]
            if index==x:
                x = j[1]
            x-=1
            #if values[index-1][i] in values[x]:
            for t in range(animal_count):
                if animal_com[values[index-1][i]][t]==0:
                    if t in values[x]:
                        values[x].remove(t)
                        if len(values[x])==0:
                            return False
    
    #assign the animal to cage
    assignment[index-1] = True
    values[index-1] = [values[index-1][i]]
    #check arc consistency
    arc_consistent = AC3(assignment , values , arc , index-1)
    #arc_consistent = True
    if arc_consistent:
        if False in assignment: # if there is unassigned cage
            index = MRV(assignment , values) # which cage?
            checked = [False] * len(values[index])
            for k in range(len(values[index])):
                lcv = LCV(copy.deepcopy(assignment),copy.deepcopy(values),index,checked) #which animal in cage?
                checked[lcv] = True
                if CSP(copy.deepcopy(assignment),copy.deepcopy(values), index , lcv , copy.deepcopy(arc))==True:
                    return True
        else:
            results.append(values)


def AC3(assignment, values , arc , index):
    #update arcs after last assignment
    for x in arc:
        if index in x:
            arc.remove(x)

    for a in arc:
        dif = 0
        for animal1_index in range(len(values[a[0]])):
            animal1 = values[a[0]][animal1_index - dif]
            is_consistant = False
            for animal2 in values[a[1]]:
                if animal_com[animal1][animal2] == 1:
                    is_consistant = True
                    break
            if not is_consistant:
                values[a[0]].remove(animal1)
                dif +=1
                if len(values[a[0]]) == 0:
                    return False

    return True


def MRV(assignment, values):
    min = 1000000
    #find first unassigned cage
    for l in range(cage_count):
        if assignment[l] == False:
            index=l
            min = len(values[l])
            break
    #find minimum remaining values
    for i in range(l+1,cage_count):
        if len(values[i]) < min and assignment[i]==False:
            min = len(values[i])
            index = i
    return index


def LCV(assignment , values , index, checked):
    conflicts=0
    minConflicts = 999999
    min_k =0
    index+=1
    for k in range(len(values[index-1])):
        if checked[k] == True:
            continue
        conflicts =0
        for j in adjacents:
            if index in j:
                x = j[0]  # cage[index] is adjacent with cage[x]
                if index==x:
                    x = j[1]
                x-=1

                for t in range(animal_count):
                    if animal_com[values[index-1][k]][t]==0:
                        if t in values[x]:
                            conflicts+=1

        if conflicts < minConflicts:
            minConflicts = conflicts
            min_k = k
    return min_k


if __name__ == "__main__":
    results = list()
    cage_count = int(input("number of cages: "))
    animal_count = int(input("number of animals: "))
    adjacent_count = int(input("number of adjacents: "))

    cage_size = list(map(int , input("cage sizes: ").split(" ")[:cage_count]))
    animal_size = list(map(int , input("animal sizes: ").split(" ")[:animal_count]))
    adjacents = list(range(adjacent_count))
    print("adjacents:")
    for i in range(adjacent_count):
        adjacents[i] = list(map(int , input().split()[:2]))

    animal_com = list(range(animal_count))
    for i in range(animal_count):
        animal_com[i] = list(map(int , input().split()[:animal_count]))

    remaining_values = list(range(cage_count))
    for i in range(cage_count):
        remaining_values[i] = list()
        for j in range(animal_count):
            if(cage_size[i]>= animal_size[j]):
                remaining_values[i].append(j)

    assignment = [False] * cage_count

    arc = list()
    for index in range(cage_count):
        for j in adjacents:
            if (index+1) in j:
                x = j[0]  # cage[index] is adjacent with cage[x]
                if (index+1)==x:
                    x = j[1]
                arc.append([index , x-1])


    index = MRV(assignment , remaining_values)
    #sys.setrecursionlimit(1000)

    t0 = time()

    checked = [False] * len(remaining_values[index])
    for k in range(len(remaining_values[index])):
        lcv = LCV(copy.deepcopy(assignment),copy.deepcopy(remaining_values),index,checked)
        checked[lcv] = True
        CSP(copy.deepcopy(assignment) , copy.deepcopy(remaining_values), index , lcv ,copy.deepcopy(arc))

    t1 = time()

    print("time: " + str(t1-t0))
    print("results:")
    for i in results:
        print(i)
