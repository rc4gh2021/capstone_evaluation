#capstone evaluation point calculator
#small light weight python to help you avoid headache calculate your points
#All you need is python3 on you machine
#Author: Rithea
#Date: 7/27/2021

P1 = input("enter your name: ")
P2 = input("enter your first teammate name: ")
P3 = input("enter your second teammate name: ")

################################################

def data_calculation(TM1,TM2,TM3):
    print()
    print(TM1.upper(),"data")
    print("Please enter between 1 and 10")
    T2 = input(TM2+"(15%): ")
    while((T2.isnumeric() == False) or float(T2)<1 or float(T2)>10):
        print("Enter between 1-10.")
        T2 = input(TM2+"(15%): ")
    T3 = input(TM3+"(15%): ")
    while((T3.isnumeric() == False) or float(T3)<1 or float(T3)>10):
        print("Enter between 1-10.")
        T3 = input(TM3+"(15%): ")
    SP = input("sponsor(15%): ")
    while((SP.isnumeric() == False) or float(SP)<1 or float(SP)>10):
        print("Enter between 1-10.")
        SP = input("sponsor(15%): ")
    CO = input("coordinator(15%): ")
    while((CO.isnumeric() == False) or float(CO)<1 or float(CO)>10):
        print("Enter between 1-10.")
        CO = input("coordinator(15%): ")
    SU = input("supervisor(40%): ")
    while((SU.isnumeric() == False) or float(SU)<1 or float(SU)>10):
        print("Enter between 1-10.")
        SU = input("supervisor(40%): ")
    myT2 = float(T2)/10*15
    myT3 = float(T3)/10*15
    mySP = float(SP)/10*15
    myCO = float(CO)/10*15
    mySU = float(SU)/10*40
    myresult = (myT2+myT3+mySP+myCO+mySU)/10
    return myresult

##############################################
P1_average = data_calculation(P1,P2,P3)
P2_average = data_calculation(P2,P1,P3)
P3_average = data_calculation(P3,P1,P2)
##############################################
totalWork = P1_average+P2_average+P3_average
P1_con = P1_average/totalWork*100
P2_con = P2_average/totalWork*100
P3_con = P3_average/totalWork*100
##############################################
P1_grade = P1_con*240/100
P2_grade = P2_con*240/100
P3_grade = P3_con*240/100
##############################################

print("\nReport:")
print("######################################")
print("Average Points:")
print(P1.upper(),": ",P1_average)
print(P2.upper(),": ",P2_average)
print(P3.upper(),": ",P3_average)
print("######################################")
print("Contribution in percentage: ")
print(P1.upper(),": ",P1_con)
print(P2.upper(),": ",P2_con)
print(P3.upper(),": ",P3_con)
print("######################################")
print("Final Grade: ")
print(P1.upper(),": ",P1_grade,"%")
print(P2.upper(),": ",P2_grade,"%")
print(P3.upper(),": ",P3_grade,"%")
print("######################################")

