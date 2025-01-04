import random, time, os

def ran( ):
  numberList = random.randint(1,91)
  return numberList

def prettyPrint():
  for row in bingocard:
    print(row)

def Card( ):
  global bingo
  numberList =[ ]
  for i in range(8):
    num = ran ( )
    while num in numberList:
      num = ran( )

      numberList.append(ran())
      numberList.sort( )

      bingocard = [ [ numberList[0], numberList[1], numberList[2]],
              [ numberList[3], "BINGO", numberList[4] ],
              [ numberList[5], numberList[6], numberList[7]] ]
      prettyPrint()

Card( )
while True:
  prettyPrint ( )
  num = int (input("Next Number:  "))
  for row in range (3):
    for item in range (3):
      if bingo[ row] [ item] == num:
        bingo[ row] [ item] = "X"

  exes = 0
  for row in bingo:
    if item in row:
      if item =="X":
        exes += 1

  if exes == 8:
    print("You are a winner")
    break

  time.sleep(1)
  os.system("clear")