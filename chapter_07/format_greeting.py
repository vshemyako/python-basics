def compose_titled_name(first_name: str, last_name: str) -> str:
    return " ".join([first_name, last_name]).title()


def greet(name: str = "Stranger") -> None:
    print("Hello, {}".format(name))


def say_goodbye() -> None:
    print("Goodbye!")


def get_quit_string() -> str:
    return "q"


def is_quit_string(input: str) -> bool:
    return get_quit_string() == input


while True:
    print("Please enter your name!")
    print("In case you don't want to proceed, enter '{}'.".format(get_quit_string()))

    first_name = input("First name: ")
    if is_quit_string(first_name):
        say_goodbye()
        break

    last_name = input("Last name: ")
    if is_quit_string(last_name):
        say_goodbye()
        break

    composed_name = compose_titled_name(first_name, last_name)
    greet(composed_name)
    print()
