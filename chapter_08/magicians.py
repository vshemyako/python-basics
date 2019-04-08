def make_great(magicians: [str]) -> [str]:
    great_template = "{} the Great"
    for index, value in enumerate(magicians):
        magicians[index] = great_template.format(value)
    return magicians


def show_magicians(magicians: [str]) -> None:
    for magician in magicians:
        print(magician)


magicians = ["Merlin", "Gandalf", "Dumbledore"]
great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
