AFFILIATE PROGRAM - LINK GENERATOR

This program helps providing affiliate program in partnership with online bookstore dedicated to IT - Helion.
After entering users ID and chosen URL, script will convert it to partner's unique version. Supported URLs include
homesite, particular products, promotions, categories and shopping cart. This program tests if entered data is an URL,
recognize type of it and after convertion saves it to file. The file 'books_register.txt' will be created if it doesn't
exist.

The program contains functions containing if statements, loops and basic file reading and writting modes.

# Saving URLs to file:
If the target file doesn't exist yet, program will create it and ask user if he needs to create simple title row,
containing simple column names. If it is not necessary, skips this step.
If the target file already exists, program will check if the title row is included in file and then ask user if he
needs to create it. If not then it will start adding old target URL and new one.

Calling/importing main() function from export.py file will initiate adding and saving process.

By: Marta Sleboda, Dominika Jastrzebska, Aleksandra Kuberska