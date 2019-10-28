import random
print("This is a name generator. ")
print()
list_vowel = "aeio"
list_vowel2 = "iuy"
list_consonants = "b c d f g h j k l m n p r s t w x z".split()
list_2consonants = ['rd', 'st', 'th', 'dr', 'wr', 'mn', 'sp', 'pr']

vowel = random.choice(list_vowel)
vowel2 = random.choice(list_vowel2)
consonants2 = random.choice(list_2consonants)
consonant = random.choice(list_consonants)

a = vowel + consonant + vowel2 + consonants2
b = consonants2 + vowel + consonant
c = consonant + vowel + consonants2
d = consonant + vowel + consonants2 + vowel2
e = vowel + consonant + vowel + consonants2
f = consonant + vowel + consonant + vowel
name_list = [a, b, c, d, e, f]
name = random.choice(name_list).capitalize()
print(f"Your new name is {name}. \n\n{name} is a praiseworthy name for a warrior.")
