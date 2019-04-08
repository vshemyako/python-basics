# Playing with return values of a function
def create_person(first_name: str, last_name: str) -> {str, str}:
    person = {"first_name": first_name, "last_name": last_name}
    return person


musician = create_person("Johnnie", "Walker")
print(musician)
