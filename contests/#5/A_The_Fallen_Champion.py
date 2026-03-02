yousefWin, yousefTime = map(int, input().split())
warriors = [(w, t) for _ in range(int(input())) for w, t in [map(int, input().split())]]

for warriorWin, warriorTime in warriors:
    if (warriorWin > yousefWin) or (warriorWin == yousefWin and warriorTime < yousefTime):
        print("The Fallen Champion")
        break
else:
    print("The Champion Saves the Accused")