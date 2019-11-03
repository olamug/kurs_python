filename1 = '20_quotes_text.txt'
# filename = input("Please insert name of file with its extension containing your quotes: \n")
print("Here you are first 5 quotes:\n")

with open(filename1, 'r', encoding='utf-8') as fopen:
    lines_list = fopen.readlines()

counter = 0
for e in lines_list:
    if counter < 5:
        counter += 1
        print(str(counter)+'.', e, end='')
    else:
        break
