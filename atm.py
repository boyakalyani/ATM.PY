print("welcome to the state bank of india")
print("insert ur card")
amount=20000
pin=1234
lan=input("enter ur lan")
pin=int(input("enter ur pin"))
if lan=="english" or "telugu" or "hindi":
    if pin==1234:
        print("1.withdrawa")
        print("2.balance enquiry")
        print("3.deposite")
        print("4.money tranfer")
        print("5.change ur pin")
        print("6.exit")
        transaction=input("enter ur transacatinon")
        withdraw=int(input("enter ur amount"))
        if withdraw<=20000 and 20000>=withdraw:
            print("collect  ur cash")
            transaction1=input("enter the transaction")
            pin1=int(input("enter ur pin"))
            if pin1==pin:
                print("ur available balance is ")
                transaction2=input("enter ur transaction")
                deposite=int(input("entere the amount"))
                total=amount+deposite
                if total>=0:
                    print("ur deposite sussfull and avatillabell balanc is",total)
                    transaction3=input("enter ur transaction")
                    money=int(input("enter ur amount"))
                    total=amount-money
                    if total>=0:
                        print("ur money sussusfuly transfer and available balance is",total)
                        transaction4=input("enter ur transaction")
                        old=1234
                        old=int(input("enter ur old pin"))
                        new=int(input("enter ur new pin"))
                        if old!=new:
                            print("ur pin changed sucussesfull")
                        else:
                            print("ur pin not changed invalid details and pin number")
                    else:
                        print("ur money not sucusseful invalid details")
                else:
                    print("ur deposite is not sussfull invalid details")
            else:
                print("ur pin is wrong")
        else:
            print("invalid cash")
    else:
        print("ur pin is wrong")
else:
    print("exit")