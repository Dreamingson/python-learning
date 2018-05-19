import random

def printInfo():
    print("本程序模拟两个选手A和B的某种竞技比赛，请输入A和B的能力值(0-1的小数)")


def getInputs():
    a = eval(input("请输入选手A的能力值："))
    b = eval(input("请输入选手B的能力值："))
    n = eval(input("请输入模拟比赛场次："))
    return a,b,n


def simNGames(n,proA,proB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(proA,proB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB


def printSummary(winsA,winsB):
    n = winsB + winsA
    print("模拟开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场,占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场,占比{:0.1%}".format(winsB,winsB/n))


def gameOver(a,b):
    if a == 15 or b == 15:
        return True
    else:
        return False

def simOneGame(proB,proA):
    scoreA,scoreB = 0,0
    serving = 'A'
    while not gameOver(scoreA,scoreB):
        if serving == 'A':
            if random.random() < proA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random.random() < proB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA,scoreB


def main():
    printInfo()
    proA, proB,n = getInputs()
    winsA, winsB = simNGames(n,proA,proB)
    printSummary(winsA,winsB)

main()