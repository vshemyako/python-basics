# getting accustomed with basic python array syntax
names = ["jake", "jones", "johnie", "ronnie"]
message_template = "Quite interesting name is {}"

# 3.1
for name in names:
    print(name)

# 3.2
for name in names:
    message = message_template.format(name.title())
    print(message)
