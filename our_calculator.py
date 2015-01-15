from arithmetic import *
def main():

    x = True 
   # while x == True: 

        cal = raw_input(">")
        cal_split = cal.split(" ")
        a = int(cal_split[1])
        b = int(cal_split[2])
      
        if cal_split[0] == "q":
           #x = False
        elif cal_split[0] == "+":
            print add(a, b)

        elif cal_split[0] == "-":
            print subtract(a, b)

        elif cal_split[0] == "*":
            print multiply(a, b)

        elif cal_split[0] == "/":
            print divide(a, b)

        elif cal_split[0] == "square":
            print square(a, b)

        elif cal_split[0] == "cube":
            print cube(a, b)

        elif cal_split[0] == "pow":
            print pow(a, b)

        elif cal_split[0] == "mod":
            print mod(a, b)
        else: 
            print "ERROR"
    

if __name__ == '__main__':
    main()