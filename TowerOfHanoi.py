# This is an example for a recursion program

def TowerofHanoi(numberofDisks, startPeg = 1, endPeg = 3):
    if numberofDisks:
        TowerofHanoi(numberofDisks - 1,startPeg,6 - startPeg - endPeg)
        print("Move disk %d from peg %d to peg %d"%(numberofDisks,startPeg,endPeg))
        TowerofHanoi(numberofDisks-1,6 - startPeg - endPeg,endPeg)

print(TowerofHanoi(3))