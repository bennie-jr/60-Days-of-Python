### DAY 6 - APP1: Build a To-do App with Python(Working with Text Files)

Today's focus was on working with text files in python.

Recap on yesterday's code. With the todo app from yesterday, I worked on improving user experience. I improved the show option by adding the enumerate function
and f-strings to the for loop which printed out a more human-readable todo list. Also added a fifth choice which was "complete" to remove completed todos. Today, I worked with only text files. So, the code 
up until yesterday only stored the todos temporarily that is if the program is exited the todos vanished as well. To fix this , I needed a place to store the todos so they can be
available even after the program exits. That is where text files comes in , I created a text file to store the todos and adjusted the code accordingly. I only worked on the add
and show case blocks for now, I introduced the open() function into the code with both read and write modes to read todos from the central storage text file 
and also write to it as well. I was able to achieve this by using the readlines() and writelines() method. Also cleared out the previous storage for the todos which was a list
and concatenated a new line to the user input to give more readability to the todo list.

I also experimented more on text files and how to manipulate them with python. Especially the open() function and using the right file paths for files I need to access. 

In today's bonus section I worked on creating text files and appending to the files with a for loop to iterate through 2 lists(one for the filename and the other for the file contents) using the zip function().

I did a few more exercises on bug fixing.

Lastly, I learned about how to find good forums and online communities dedicated to python only.


Overall, the sixth day was quite an experience, I learned something new. I will keep building on the to-do app making it more robust in the coming days.