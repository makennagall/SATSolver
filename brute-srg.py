#!/usr/bin/env python3

# this file is for the brute force SAT Solver

def main():

    # reading in file with comments
    #SATcfile = open('kSAT.cnf', 'r')

    #Lines = SATcfile.readlines()
    #test smaller file:
    testcFile = open('oneTest.cnf', 'r')
    Lines = testcFile.readlines()
    # number of variables
    variables = []

    # number of clauses
    clauses = []

   # int i = 0
    testDict = createDictionary(5)
    allPossibilities(5, testDict, [])

    # ignore lines with comments for testing purposes
    for line in Lines:
        if(line.startswith('p')):
            # split the line to obtain variables and clauses
            elements = line.split()
            variables.append(int(elements[2]))
            clauses.append(int(elements[3]))
    #print("variables: " ,variables)
    #print("clauses: ", clauses)
    clauseList = []
    for line in Lines:
        if line.startswith('c'):
            #if the list of clauses is not empty, evaluate the clauses:
            if bool(clauseList):
                varDict = {}
                #print("Variables: ", numVariables, "\t Clauses: ", numClauses)
                varDict = createDictionary(numVariables)
                allPossibilities(numVariables, varDict, clauseList)
                clauseList = []
            print(line)
            pItems = line.split()
            satisfiability = pItems[3]
            if satisfiability == 'U':
                print("should be unsatisfiable")
            else:
                print("should be satisfiable")
        if(line.startswith('p')):
            elements = line.split()
            numClauses = int(elements[3])
            numVariables = int(elements[2])
        if not line.startswith('c') and not line.startswith('p'):
            clauseList.append(line)
#evaluates last test:
    varDict = {}
    varDict = createDictionary(numVariables)
    allPossibilities(numVariables, varDict, clauseList)


    #test of createDictionary, allPossibilities and printDict:
def createDictionary(numVars):
    #keys are numbers 1 to the number of vars (representing x1, x2 ... xnumVars)
    varDict = {}
    for i in range(1,numVars + 1):
        #initialize all values to True
        varDict[i] = True
    return varDict


def allPossibilities(numVars, varDict, clauseList):
    #range consists of numbers 0 through 2^numVars - 1
    #iterates 2^numVar times
    for i in range(1, pow(2, numVars)+1):
        print(i, " : ", end= "")
        #iterates numVar times
        for j in range(numVars):
            if(i%pow(2,j) == 0):
                if varDict[j+1]:
                    varDict[j+1] = False
                else:
                    varDict[j+1] = True
        printVars(numVars, varDict)
        if evalClauses(numVars, varDict, clauseList):
            print("Satisfiable")
            printVars(numVars, varDict)
            return True
    print("Unsatisfiable")


def printVars (numVars, varDict):
    for i in range(1, numVars + 1):
        #print all values
        print(i,  varDict[i], end="; ")
    print()


def evalClauses(numVars, varDict, clauseList):
    for clause in clauseList:
        #print("clause: ", clause, end="")
        currClause = False
        for var in clause.split(',')[:-1]:
            #print("var being tested: ", var)
            if int(var) < 0:
                if not varDict[abs(int(var))]:
                    #print(var, ": " ,varDict[abs(int(var))])
                    currClause = True
            elif int(var) > 0:
                if varDict[abs(int(var))]:
                    #print(var, ": " ,varDict[abs(int(var))])
                    currClause = True

        if not currClause:
            print("did not pass this clause", end=" ")
            printVars(numVars, varDict)
            return False
        else:
            print("passed this clause")
    print("worked: ", end=" ")
    printVars(numVars, varDict)
    return True

if __name__ == "__main__":
    main()
