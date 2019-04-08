def compose_address_string(city: str, country: str) -> str:
    address_template: str = "{}, {}"
    return address_template.format(city, country).title()


print(compose_address_string("brussels", "belgium"))
print(compose_address_string("havana", "cuba"))
print(compose_address_string("lisbon", "portugal"))
