### DAY 8 - APP1: Build a To-do App with Python(With-Context Manager)

Today, I worked on optimising the code base mostly with the With-Context Manager.

Recap on yesterday's code. With the todo app from yesterday, I worked on making the program output a bit user-friendly with list comprehension. Today, I optimised the code with the with-context manager. The previous code had a few lines of code for 
file manipulation with the open() function, and the lines always had to end with the .close() method. I improved on those lines of code on file manipulation by using the With-Context manager. The great thing about using this context manager 
is that it helped me reduce the lines of code for file manipulation and made the code more readable and also, this time I don't need to end with the .close() method. The context manager calls it implicitly under the hood. Also introduced edit and complete 
case blocks to the With-Context Manager and fixed the code to use the central storage i.e the text file for its respective manipulations. The previous code didnt have the text file operations for the edit and complete blocks and always threw an
error when those blocks ran. So, fixing those blocks made the every part of the code run smoothly.

I also experimented more on the With-Context Manager.

In today's bonus section I worked on a journaling program.The program asks for current date and creates a .txt file using the date. The program then asks for your mood on a scale of 1-10 and then proceeds to let you write down your thoughts and 
appends to the .txt file it created.

I did one exercise on bug fixing.

Lastly, I learned about the steps involved in creating and maintaining a program. I learned that you always start with a simple minimum value product and then build on it by adding features, fixing bugs and optimising code based on customer or consumer
feedback, and then you keep the loop of improving features, fixing bugs and optimising code going to continue giving consumers the best service.


Overall, day 8 was quite okay, I learned something new. I will keep building on the to-do app making it more robust in the coming days.