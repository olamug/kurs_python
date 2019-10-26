import random
print("This is a name generator. ")
print()
list_vowel = "a e i o u y".split(" ")
list_consonants = "b c d f g h j k l m n p r s t w x z".split()
list_2consonants = ['rd', 'st', 'th', 'dr', 'wr', 'mn', 'sp', 'pr']

vowel = random.choice(list_vowel)
consonants2 = random.choice(list_2consonants)
consonant = random.choice(list_consonants)

a = vowel + consonant + vowel + consonants2
b = consonants2 + vowel + consonant
c = consonant + vowel + consonants2
d = consonant + vowel + consonants2 + vowel
name_list = [a, b, c, d]
name = random.choice(name_list).capitalize()
print(f"Your new name is {name}. \n\n{name} is a praiseworthy name for a warrior.")
