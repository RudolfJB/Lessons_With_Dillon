# first OOP


class first_oop():
    def __init__(self, **kw):
        super(first_oop, self).__init__(**kw)

    def call_back(self, data):
        # print("call back", str(data))
        cb_list = data.split(" ")
        for i in cb_list:
            print("cb: ", str(i))

    def main(self):
        print("first name")
        while True:
            cmd = input("command>>")
            if "Q" == cmd.upper():
                return

            if "cb" in cmd:
                self.call_back(cmd)


if __name__ == "__main__":
    foo = first_oop()
    foo.main()
