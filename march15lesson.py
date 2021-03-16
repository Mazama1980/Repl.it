def contacts():
    fh = open("data/contacts.txt")
    contents = fh.read()
    fh.close()
    print(contacts)



def hello():
    hello = ["Hello",
             "world",
    ]
    fh = open("data/hello.txt", "w")
    for item in hello:
        fh.write(f"{item}\n")
    fh.close()


def goodbye():
    fh = open("data/goodbye.txt", "w")
    fh.write("See ya!\n")
    fh.close()


def vie_gates():
    fh = open("data/hello.txt", "a")
    fh.write("How's it goin'?\n")
    fh.close()


def path():
    fh = open("data/data/contacts.txt")
    contents = fh.read()
    fh.close()
    print(contents)


contacts()
hello()
goodbye()
vie_gates()
path()