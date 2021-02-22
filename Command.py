import sys

def Addition(no1,no2):
    ret = no1+no2
    return ret

def main():

    #filter
    if((len(sys.argv) < 3) or (len(sys.argv) > 3)) :
        print("Invalid number of arguments")

    print("Numbr of args: ",len(sys.argv))

    ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
    print("Addition of {} and {} is {} :".format(sys.argv[1],sys.argv[2],ret))

if __name__ == "__main__":
    main()


#command to execute
#python Command.py 10 20