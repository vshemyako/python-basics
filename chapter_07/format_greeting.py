def compose_titled_name(first_name: str, last_name: str) -> str:
    return " ".join([first_name, last_name]).title()


def greet(name: str = "Stranger") -> None:
    print("Hello, {}".format(name))


def getQuitString() -> str:
    return "q"


def isQuitString(input: str) -> bool:
    return getQuitString() == input


while True:
    print("Please enter your name!")
    print("In case you don't want to proceed, enter '{}'}.".format(getQuitString()))

    first_name = input("First name: ")
    if isQuitString(first_name):
        break

    last_name = input("Last name: ")
    if isQuitString(last_name):
        break

    composed_name = compose_titled_name(first_name, last_name)
    greet(composed_name)
