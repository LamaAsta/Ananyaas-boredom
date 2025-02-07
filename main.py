import number_screen
import choice
import puzzle

wash = choice.washWindow()

def run():
    puzzle.game.new()
    puzzle.game.run()
    t = puzzle.random.randint(1,2)
    w1 = number_screen.WaitScreen(t)
    w1.run()
    ch = choice.choiceWindow()
    ch.new()
    c = ch.run()
    timeTaken1 = ch.timeTaken()
    print("TIME1: ",timeTaken1)
    g1 = puzzle.Game(n = c)
    g1.new()
    g1.run()

    wash.new()
    wash.run()

    if t == 1:
        w2 = number_screen.WaitScreen(2)
    else:
        w2 = number_screen.WaitScreen(1)
    w2.run()

    ch2 = choice.choiceWindow()
    ch2.new()
    c = ch2.run()
    timeTaken2 = ch2.timeTaken()
    print("TIME2: ",timeTaken2)
    g1 = puzzle.Game(n = c)
    g1.new()
    g1.run()


if __name__ == '__main__':
    run()
