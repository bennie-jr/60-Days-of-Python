### DAY 13 - APP1: Build a To-do App with Python(Utilizing Default Arguments)

Today, I continued with avoiding code repetition by using functions and introduced default arguments.

Recap on yesterday's code. With the todo app from yesterday, I added another function to write to the text file
hereby eliminating the need to have various open builtin functions for writing to the text file in the code base.
I also introduced multiple  arguments for the write todos function which included the filepath and the todos list
that would be written to the file. Today, I introduced default arguments in the code base. So with the previous code,
all the points in the code I called the write or read function had one thing in common they all had the text file as
the argument. I added the text file to the main functions as a default argument so I wouldn't have to keep adding the
text file as an argument everytime I call the function. I also learned the right way to place default and non-default
arguments in a function. The last thing I added to the code today was docstrings to briefly describe what the 
functions did.

I also experimented more on docstrings.

In today's bonus section I built on the function I wrote previously which converts feet inches to meters and calls the 
function in an if else condition to check the height of kids at a theme park. I added a second function which grabs the 
values, prepares and returns them to be converted by the other function. This built on my knowledge on decoupling. So, with 
this program, I decoupled the function and decoupled the output as well and this helped me call the variables I returned 
anywhere in the code which I could not do previously.

I did one exercise on bug fixing.

Lastly, I learned about the various python version including the major, minor and patch. I also learned about which of the
3(major,minor,patch) had backwards compatibility and also the kind of implications the update in version has on your
existing code base.

All in all, day 13 was okay, I learned something new. I will keep building on the to-do app making it more robust in the coming days.