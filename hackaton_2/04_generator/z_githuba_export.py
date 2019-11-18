import os.path

register = 'books_register.txt'


def add_title_row():
    with open(register, 'w', encoding='utf-8') as r:
        col = [f'{input("Enter name of the first column: ")}, {input("Enter name of the second column: ")}', '\n']
        columns = ','.join(col)
        r.write(columns)


def another_link():
    answer = input('Press A to add next link, press F to finish your work.')
    if answer.lower() == 'a':
        return True
    else:
        print('Your data has been successfully saved.')
        return False


def create_register():
    original_url = input('Enter original url: \n')
    new_url = input('Enter new url: \n')
    construction = [original_url, new_url, '\n']
    list = ','.join(construction)
    return list


def add_register(list):
    with open(register, 'a+', encoding='utf-8') as r:
        r.writelines(list)

    while another_link() == True:
        create_register()


def main():
    with open(register, 'w+', encoding='utf-8') as r:
        content = r.readline()
        if content == '':
            title_answer = input('Title row is not created. Press C to create it now. '
                                 'Press S to skip and add your links.')
            if title_answer.lower() == 'c':
                add_title_row()
        # elif 'old links' and 'new links' in content:
        #     title_answer = input('Title row is not created, but your list already contains data. '
        #                          'Press C to create it now. Press S to skip and add your links.')
        #     if title_answer.lower() == 'c':
        #         with open(register, 'r', encoding='utf-8') as r:
        #             content = r.readlines()
        #         col = ['OLD LINKS', 'NEW LINKS', '\n']
        #         col = ','.join(col)
        #         output_content = col + content
        #         with open(register, 'w', encoding='utf-8') as r:
        #             r.writelines(output_content)
    register_list = create_register()
    add_register(register_list)


main()