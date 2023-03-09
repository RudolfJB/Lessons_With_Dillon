# first OOP


class first_oop():
    def __init__(self, **kw):
        super(first_oop, self).__init__(**kw)

    def main(self):
        print("first name")
        while True:
            cmd = input("command>>")
            if "Q" == cmd.upper():
                return
            else:
                print(cmd)


if __name__ == "__main__":
    foo = first_oop()
    foo.main()
