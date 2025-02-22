import number_screen
import choice
import puzzle
import time
import os 

COMPLETE_TIME = 60*1
BaseTime = 0.5

def halfPart(t):
    w1 = number_screen.WaitScreen(t)
    w1.run()
    bored = choice.boredWindow()
    bored.new()
    boredLevel = bored.run()
    ch = choice.choiceWindow()
    ch.new()
    c = ch.run()
    timeTaken = ch.timeTaken()
    g1 = puzzle.Game("raw2.jpeg",n = c)
    completed = 0
    elapsed = 0
    timer = time.time()
    if c == 6:
        g1.new()
        completed = g1.run()
    else:
        s = time.time()
        while time.time() - s <= COMPLETE_TIME :
            g1.new()
            completed = g1.run()
    elapsed = time.time()-timer
    return c,timeTaken,boredLevel,completed,elapsed


def writter(*args):
    ls = os.listdir("./")
    if 'results.csv' not in ls:
        a = open('results.csv',"w+")
        a.write("PID,Time1,BoredLevel,choiceRT,choice made,Completed,PuzzleTime,Time2,BoredLevel,choiceRT,choice made,Completed,PuzzleTime\n")
        a.close()
    a = open('results.csv','a')
    s = ','.join([str(i).strip(" ' ") for i in args])[1:-1]
    print(s)
    a.write(s+'\n')
    a.close()

def run():
    participant = choice.participantWindow()
    participant.new()
    pID = participant.run()

    print("PID: ",pID)

    # puzzle.game.new()
    # puzzle.game.run()

    t = puzzle.random.randint(1,2)
    if t == 1:
        t1 = 2*BaseTime 
    else:
        t1 = 4*BaseTime
    
    c1, Tt1, b1, com1, e1 = halfPart(t1)

    wash = choice.washWindow()
    wash.new()
    wash.run()

    

    if t == 1:
        t2 = 4*BaseTime 
    else:
        t2 = 2*BaseTime 

    c2, Tt2, b2, com2, e2 = halfPart(t2)

    return pID,t1,b1,Tt1,c1,com1,e1,t2,b2,Tt2,c2,com2,e2


if __name__ == '__main__':
    ar = run()
    writter(ar)
    print("write succesful")
