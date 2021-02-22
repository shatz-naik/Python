
import Arithmetic


def main():
    no1 = int(input("Enter first no :"))
    no2 = int(input("Enter second no :"))

    ret = Addition(no1,no2)
    print("Addition is:",ret)

    print("Addition of {} and {} is {}".format(no1,no2,ret))

    ret = Arithmetic.Substraction(no1,no2)
    print("Substraction of {} and {} is {}".format(no1,no2,ret))

#starter of main

if __name__ == "__main__":
    main()