def make_shirt(text: str = "I love Python", size: int = 30) -> None:
    shirt_logo_template = "Printed '{}' of '{}' size"
    print(shirt_logo_template.format(text, size))


make_shirt("Pythonic python", 30)
make_shirt(size=20, text="Dynamically typed language")
make_shirt()
make_shirt("I don't like Python")
make_shirt(size=25)
