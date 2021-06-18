# Django Toy Project

## Objective
A CRUD application for learning Django.

This application demonstrates a Library Management System consisting of an admin and several users. The admin must be able to perform CRUD operations on all books and users. The users should be able to perform CRUD operations on books.

The main objective of this project is to develop an authentication system for the admin and the users and also to enable CRUD operations by both parties.

## Contents
The contents of this directory include:

- **src**: This folder contains the project directories and files.
- **createdb.sql**: This file contains the SQL script to create the database for the project.
- **drop_db**: This file contains the SQL script to delete the database created for the project after use.
- **README.md**: This is the file we are in. It contains details about this project, its files and specific instructions on how to run the code.
- **requirements.txt**: This file contains all the dependencies that need to be installed prior to running the code.
- **USER-STORIES.md**: This file contains the user stories for the project.

## Instructions to run the code

1. Create a separate directory for this project using ```mkdir```.
2. Clone the project using the submitted URL using ```git clone``` inside this directory.
3. Create a virtual environment for the project using ```virtualenv``` and activate it.
4. Ensure that all dependencies have been downloaded from ```requirements.txt``` file.
5. Enter the project directory using ```cd```.
6. Open Postgres prompt using ```sudo -u postgres psql```.
7. Type ```\i create_db.sql``` to create the database for the project. Type ```\q``` to exit this prompt.
8. Type ```cd src``` to enter the source directory.
9. In the terminal, type ```python manage.py makemigrations``` to get the data ready for transfer.
10. Then type ```python manage.py migrate``` to transfer the data to the database.
11. To create a superuser, type ```python manage.py createsuperuser```.
12. Follow the prompts to create superuser name and password. (Email can be skipped).
13. To run the server, type ```python manage.py runserver```. A link will appear.
14. Copy this link and paste in your browser. It will open the user login page.
15. Append only ```admin``` after the link to open the admin login page.
16. Here, you can perform CRUD operations as an admin.
17. Logout and go to ```/login``` page.
18. Sign up new user by entering the required details.
19. Login using these credentials to view customer dashboard.
20. Visit the admin page again to add this user as a customer. Return to the user dashboard.
21. Here, you can perform CRUD operations as a user.
22. After inspection, close the browser tab.
23. Return to the terminal and press ```Ctrl + C``` to stop the server.
24. Type ```cd ..``` to go back one level in the directory structure.
25. Repeat Step 6.
26. Type ```\i drop_db.sql``` to drop the database for the project. Type ```\q``` to exit this prompt.
27. Type ```deactivate``` to deactivate the virtual environment.


## Notes

1. Dependencies that need to be installed have been included in the requirements.txt file.
2. The admin will have to add a user as a customer before that user can perform CRUD operations.