import number_screen
import choice
import puzzle
import time
import os 


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
    g1 = puzzle.Game("../raw2.jpeg",n = c)
    if c == 2:
        s = time.time()
        while time.time() - s <= 10 :
            g1.new()
            g1.run()
    if c == 6:
        g1.new()
        g1.run()
    return c,timeTaken,boredLevel


def writter(*args):
    ls = os.listdir("./")
    if 'results.csv' not in ls:
        a = open('results.csv',"w+")
        a.write("PID,Time1,choiceRT,choice made,Time1,choiceRT,choice made\n")
        a.close()
    a = open('results.csv','a')
    s = ','.join([str(i).strip(" ' ") for i in args])[1:-2]
    print(s)
    a.write(s+'\n')
    a.close()

def run():
    participant = choice.participantWindow()
    participant.new()
    pID = participant.run()

    print("PID: ",pID)

    puzzle.game.new()
    puzzle.game.run()

    t = puzzle.random.randint(1,2)
    
    c1, Tt1, b1 = halfPart(t)

    wash = choice.washWindow()
    wash.new()
    wash.run()

    

    if t == 1:
        t2 = 2
    else:
        t2 = 1

    c2, Tt2, b2 = halfPart(t2)

    return pID,c1,Tt1,b1,c2,Tt2,b2


if __name__ == '__main__':
    ar = run()
    writter(ar)
    print("write succesful")
