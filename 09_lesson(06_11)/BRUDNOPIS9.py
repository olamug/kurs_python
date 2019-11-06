def email_search(users_email):
    if users_email in email_list:
        print("Znaleziono! Pod numerem", (email_list.index(users_email) + 1))
    else:
        print("Twojego maila nie ma na liście.")


email_list = ["a@gmail.com", "b@gmail.com", "c@gmail.com"]
input_email = input("Podaj swój e-mail: ")

email_search(input_email)




# for e in range(len(email_list)):
#     if users_email == email_list[e]:
#         print("Znaleziono! Email nr", e+1)
#         break
#     elif e == len(email_list) and users_email != email_list[e]:
#         print("Twojego maila nie ma na liście.")