start of the new project
first initial thing which is user interface is done and more work is still there like data storing and getting them in right place but the initial version is done where we can talk or interact with it
and it is completely cli based project i am not sure i will go for further in this project
the initial version contains and input and respond system where you will have 3 options
1.register if you are a new user
2.login if you have your id and password and for now i don't have password authentication system yet
3.exit where you want to end the program

todays update is that i worked on registration and login where i saved the data of the new user in a dictionary and later i added that data to a json file
13\07\26
i'm having some issues with organizing files in this project and today i'll solve this problem 
main thing to be noticed is which file contains what that's the main question here and i did some mistakes too till now and time to correct
todays tasks are as follows
1.organize the files according and comment down the things which will be there
2.update on git and github
till now a lot of changes happened in the code base and it took  a lot of time for this
major changes happened
auth register and login and exit these functions moved to auth and it handles the registration process 
file_manages handles the loading saving information
user represents a user and create a new user whenever function is called
main handles the input operations
authentication almost done with some minor changes remaining like i want connect things to other files so work is still incomplete
problem is how i connect them like i want to show the dashboard of the user who logged in and for that i want confirmation from the
login or from the authentication
the first solution i found is to write a series of code or block of code in dash file where i can easily access the confirmation from the login but the i can't because the login block should be in auth and it will be there
so other classic method is get the user id of the person logged in from the login func and then search the user in the data base finally show the dashboard of the user if he want to
till now the register and login things are working accordingly and has no errors and i am gonna implement try error blocks there for 
and new case scenarios like i want to add exception handling here..