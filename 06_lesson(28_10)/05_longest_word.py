filename = 'tekst.txt'

with open(filename, 'r', encoding='utf-8') as fopen:
    content = fopen.read()
    content = (content.replace(".", '')).replace(",", "")
    content = content.split()
print(content)

largest = ''
for e in content:
    if len(e) > len(largest):
        largest = e

print('Najdłuższe słowo/słowa to: ')
for e in content:
    if len(e) == len(largest):
        print(e)