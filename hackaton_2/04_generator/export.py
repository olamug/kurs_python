import os.path

register = 'books_register.txt'


def add_title_row():
    with open(register, 'w', encoding='utf-8') as r:
        col = ['OLD LINK', 'NEW LINK', '\n']
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
    row = ','.join(construction)
    return row


def add_register(list):
    with open(register, 'a+', encoding='utf-8') as r:
        r.writelines(list)
    while another_link():
        create_register()


def intro():
    # with open(register, 'w+', encoding='utf-8') as r:
    #     content = r.readline()
    #     if not 'original links' and 'new links' in content.lower():
    #         pass
    #     elif content == '':
    #         title_answer = input('Title row is not created. Press C to create it now. '
    #                              'Press S to skip and add your links.')
    #         if title_answer.lower() == 'c':
    #             add_title_row()
    #     else:
    #         title_answer = input('Title row is not created, but your list already contains data. '
    #                              'Press C to create it now. Press S to skip and add your links.')
    #         if title_answer.lower() == 'c':
    #             with open(register, 'r', encoding='utf-8') as r:
    #                 content = r.readlines()
    #             col = ['OLD LINK', 'NEW LINK', '\n']
    #             col = ','.join(col)
    #             content = col + content
    #             with open(register, 'w', encoding='utf-8') as r:
    #                 r.writelines(content)
    register_list = create_register()
    add_register(register_list)


if __name__ == "__main__":
    intro()
