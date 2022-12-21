#defining the amounts of coins
Onepamount = 0
Twopamount = 0
Fivepamount = 0
Tenpamount = 0
Twentypamount = 0
Fiftypamount = 0
Onepoundamount = 0
Twopoundamount = 0

while True:
    onoroff=input("Would you like to use the program?")
    if onoroff == "yes" or "Yes" or "YES" or "yES" or "YeS" or "yEs" :
        bagWeight = input("What is the weight of your bag in grams?")
        while True:
            if bagWeight != int:
                break
            else:
                bagWeight = input("please type in a valid amount")#getting wieght of bag and checking if number typed is valid

        coinType = input("What type of coin is in the bag? type in 1p,2p,5p,10p,20p,50p,£1,£2?")
        while True:
            if coinType == "1p" or coinType == "2p" or coinType == "5p" or coinType == "10p" or coinType == "20p" or coinType == "50p" or coinType == "£1" or coinType == "£2":
                break
            else:
                coinType = input("Please type in either,1p,2p,5p,10p,50p,£1 or £2")
        # creating a file to keep track of how many times the program runs
      
        Log = open("log.txt", "r")

        countString = Log.readline(1)
        Count = int(countString)
        Log.close()

        Log = open("log.txt", "w")
        Log.write(str(Count + 1))
        Log.close()
        # defining wieghts of coins
        Onepweight = 3.56
        Twopweight = 7.12
        Fivepweight = 3.25
        Tenpweight = 6.50
        Twentypweight = 5.00
        Fiftypweight = 8.00
        Onepoundweight = 9.50
        Twopoundweight = 12.00

        # dividing bagweight by weight of the type of coin to find the amount of coins in the bag
        if coinType == "1p":
            NumOfCoinsInBag = int(bagWeight) / Onepweight
        if coinType == "2p":
            NumOfCoinsInBag = int(bagWeight) / Twopweight
        if coinType == "5p":
            NumOfCoinsInBag = int(bagWeight) / Fivepweight
        if coinType == "10p":
            NumOfCoinsInBag = int(bagWeight) / Tenpweight
        if coinType == "20p":
            NumOfCoinsInBag = int(bagWeight) / Twentypweight
        if coinType == "50p":
            NumOfCoinsInBag = int(bagWeight) / Fiftypweight
        if coinType == "£1":
            NumOfCoinsInBag = int(bagWeight) / Onepoundweight
        if coinType == "£2":
            NumOfCoinsInBag = int(bagWeight) / Twopoundweight

        # displaying difference and amount of coins to be subtracted or added
        if NumOfCoinsInBag != int and coinType == "1p":
            Correctwieght = 356
            Coinsneeded = (Correctwieght / Onepoundweight) - NumOfCoinsInBag#divides correct wieght by wieght of 1 coin
            print(" 1p Coins needed/need to be taken away")
            print(Coinsneeded)
            Onepamount += Coinsneeded#adds number of coins needed to the amount of coins

        if NumOfCoinsInBag != int and coinType == "2p":
            Correctwieght = 356
            Coinsneeded = (Correctwieght / Onepoundweight) - NumOfCoinsInBag
            print("2p Coins needed/need to be taken away")
            print(Coinsneeded)
            Twopamount+= Coinsneeded

        if NumOfCoinsInBag != int and coinType == "5p":
            Correctwieght =325
            Coinsneeded = (Correctwieght / Onepoundweight) - NumOfCoinsInBag
            print("5p Coins needed/need to be taken away")
            print(Coinsneeded)
            Fiftypamount += Coinsneeded

        if NumOfCoinsInBag != int and coinType == "10p":
            Correctwieght = 325
            Coinsneeded = (Correctwieght / Onepoundweight) - NumOfCoinsInBag
            print("10p Coins needed/need to be taken away")
            print(Coinsneeded)
            Tenpamount += Coinsneeded

        if NumOfCoinsInBag != int and coinType == "20p":
            Correctwieght = 250
            Coinsneeded = (Correctwieght / Onepoundweight) - NumOfCoinsInBag
            print("20p Coins needed/need to be taken away")
            print(Coinsneeded)
            Twentypamount+= Coinsneeded

        if NumOfCoinsInBag != int and coinType == "50p":
            Correctwieght =208
            Coinsneeded = (Correctwieght / Onepoundweight) - NumOfCoinsInBag
            print("50p Coins needed/need to be taken away")
            print(Coinsneeded)
            Fiftypamount+= Coinsneeded

        if NumOfCoinsInBag != int and coinType == "£1":
            Correctwieght = 190
            Coinsneeded = (Correctwieght / Onepoundweight) - NumOfCoinsInBag
            print("£1 Coins needed/need to be taken away")
            print(Coinsneeded)
            Onepamount +=Coinsneeded

        if NumOfCoinsInBag != int and coinType == "£2":
            Correctwieght = 120
            print(str(int(bagWeight) - Correctwieght) + " -difference")
            Coinsneeded= (Correctwieght/Twopoundweight) - NumOfCoinsInBag
            print("£2 Coins needed/need to be taken away")
            print(Coinsneeded)
            Twopoundamount += Coinsneeded

        Log = open("log.txt", "r")
        content=Log.read()
        print(content + "-number of bags")#Reads the number of times the program runs and prints it to console

        print(str(Twopoundamount)+"Amount of £2s added/subtracted")
        print(str(Onepoundamount)+"Amount of £1s added/subtracted")
        print(str(Fiftypamount)+"Amount of 50ps added/subtracted")
        print(str(Twentypamount) + "Amount of 20ps added/subtracted")
        print(str(Tenpamount) + "Amount of 10ps added/subtracted")
        print(str(Fivepamount) + "Amount of 5ps added/subtracted")
        print(str(Twopamount) + "Amount of 2ps added/subtracted")
        print(str(Onepamount) + "Amount of 1ps added/subtracted")

    if onoroff == "no":#resets all values to 0 and ends the loop
        Onepamount = 0
        Twopamount = 0
        Fivepamount = 0
        Tenpamount = 0
        Twentypamount = 0
        Fiftypamount = 0
        Onepoundamount = 0
        Twopoundamount = 0
        Log = open("log.txt", "w")
        Log.write(str(Count - Count))
        break


