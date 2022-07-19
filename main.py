import random
import string

system_random = random.SystemRandom()
file1 = open("output.txt", "w+")
text = input("Text to obfuscate:")
l = input("Length:")

if l.isnumeric() is False:
    raise TypeError("Only digits and full numbers are allowed")

l = int(l)

if round(l / 3) == l:
    raise TypeError("Only multiples of 3 are accepted")

nf = round(l / 3)


def insert_sting_middle(str, word, pos):
    return str[:pos] + word + str[pos + len(word):]


# select digits at random
digits = random.choices(string.digits, k=nf)

# select uppercase letters at random
letters = random.choices(string.ascii_uppercase, k=nf)

# select lowercase letters at random
low_letters = random.choices(string.ascii_lowercase, k=nf)

# shuffle both letters + digits
sample = random.sample(digits + letters + low_letters, l)

result = ''.join(sample)
pos = system_random.randint(int(l / 3), int(l - (l / 3)))
result = insert_sting_middle(result, text, pos) + "S" + str(pos) + "P" + str(pos+len(text))
file1.write(result)
