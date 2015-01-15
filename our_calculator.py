from arithmetic import *
from sys import exit
def main():


   while True: 

        cal = raw_input(">")

        if cal == "q":
            exit()
        
        else: 
            cal_split = cal.split(" ")
    
            cal_split[:] = [x for x in cal_split if x != ""]

            a = float(cal_split[1])
            b = float(cal_split[2])


            if cal_split[0] == "+":
                print add(a, b)

            elif cal_split[0] == "-":
                print subtract(a, b)

            elif cal_split[0] == "*":
                print multiply(a, b)

            elif cal_split[0] == "/":
                if b == 0:
                    print "ERROR: divison by 0 is not possible."
                else:
                    print divide(a, b)

            elif cal_split[0] == "square":
                print square(a, b)

            elif cal_split[0] == "cube":
                print cube(a)

            elif cal_split[0] == "pow":
                print pow(a, b)

            elif cal_split[0] == "mod":
                print mod(a, b)
            else: 
                print "ERROR"


if __name__ == '__main__':
    main()