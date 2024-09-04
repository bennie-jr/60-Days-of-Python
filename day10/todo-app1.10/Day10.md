### DAY 10 - APP1: Build a To-do App with Python(Robust Code with Try-Except)

Today, I worked on fixing two bugs and improving user experience with error handling(try-except).

Recap on yesterday's code. With the todo app from yesterday, I improved user experience and optimised the code by removing the multiple
input methods and replaced the match case block with if-elif-else conditionals.This allowed the user to just add whatever it is they wanted
to do straight to the options. I also used list slicing method to append the changes the user wanted to make to the list and exclude 
the option since it was all bundled up in one string. Today, I fixed two bugs in the code. The first one was in the if conditional for adding a todo.
There was no line breaks when adding more than one todo so, I concatenated a line break where the todo is being appended to the list. The second 
was with the if,elif,else block. The previous code looked for the options(add,show,edit,complete) anywhere in the user input and this was creating problems
so to fix this I added the .startswith('input option here') method to apply to the option at the start of the user input and this fixed it.
I also added error handling (Try-Except) to the edit and complete option blocks to handle invalid inputs by keeping the code running and not breaking to 
improve user experience.

I also experimented more on try-except error handling and looked more into python syntax errors and logical error and how to identify them.

In today's bonus section I wrote a program that calculates the area of a rectangle. This program basically was to help me have a better understanding 
on error handling. I used the Try-Except block and an if statement with the .exit() method to handling a special case only a human can spot and that is
the user calculating for a square and not a rectangle.

I did a few exercises on bug fixing.

Lastly, I learned about cloud IDEs, their benefits and limitations. I explored Repl which is one of the numerous IDEs. 

Overall, day 10 was good, I learned something new. I will keep building on the to-do app making it more robust in the coming days.