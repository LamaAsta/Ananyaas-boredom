import number_screen
import choice
import puzzle




def run():
    participant = choice.participantWindow()
    participant.new()
    pID = participant.run()

    print("PID: ",pID)

    puzzle.game.new()
    puzzle.game.run()
    t = puzzle.random.randint(1,2)
    w1 = number_screen.WaitScreen(t)
    w1.run()
    bored = choice.boredWindow()
    bored.new()
    boredLevel1 = bored.run()
    ch = choice.choiceWindow()
    ch.new()
    c = ch.run()
    timeTaken1 = ch.timeTaken()
    print("TIME1: ",timeTaken1)
    print("Bored1: ",boredLevel1)
    print(t)
    g1 = puzzle.Game("../raw2.jpeg",n = c)
    if c == 2:
        for i in range(20):
            g1.new()
            g1.run()
    if c == 6:
        g1.new()
        g1.run()

    wash = choice.washWindow()
    wash.new()
    wash.run()

    if t == 1:
        t2 = 2
    else:
        t2 = 1
    w2 = number_screen.WaitScreen(t2)
    w2.run()
    bored = choice.boredWindow()
    bored.new()
    boredLevel2 = bored.run()
    ch2 = choice.choiceWindow()
    ch2.new()
    c = ch2.run()
    timeTaken2 = ch2.timeTaken()
    print("TIME2: ",timeTaken2)
    print("Bored2: ",boredLevel2)
    print(t2)

    g1 = puzzle.Game("../raw1.jpeg",n = c)
    if c == 2:
        for i in range(20):
            g1.new()
            g1.run()
    if c == 6:
        g1.new()
        g1.run()
    g1.new()
    g1.run()


if __name__ == '__main__':
    run()
