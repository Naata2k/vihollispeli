import secrets, string
alphabet = string.ascii_letters
print("Salasana:",''.join(secrets.choice(alphabet) for x in range(8)))