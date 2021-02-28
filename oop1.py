
class Demo:
    x = 10
    y = 20
    def __init__(self):
        print("inside constructor")
        self.i = 30
        self.j = 40


    def __del__(self):
        print("inside destructor")

    def fun(self):
        print("inside fun")


def main():
    obj1 = Demo()
    obj2 = Demo()

    obj1.fun()
    del obj1
    obj1.fun()


if __name__ == "__main__":
    main()