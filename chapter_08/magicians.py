def make_great(magicians: [str]) -> [str]:
    great_template = "{} the Great"
    for index, value in enumerate(magicians):
        magicians[index] = great_template.format(value)


def show_magicians(magicians: [str]) -> None:
    for magician in magicians:
        print(magician)


magicians = ["Merlin", "Gandalf", "Dumbledore"]
make_great(magicians)
show_magicians(magicians)
