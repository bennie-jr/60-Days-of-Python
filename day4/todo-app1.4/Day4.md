### DAY 4 - APP1: Build a To-do App with Python(List Indexing and Tuples)

Today's focus was on python List Indexing and Tuples only.

Recap on yesterday's code. With the todo app from yesterday, I built on the previous code by making the code a little more intelligent. I gave the user 3 choices (add, show and exit) with each choice having a use case.
Today, I picked up from where I left off by making the program a bit more intelligent than yesterday. I added a fourth choice which was Edit. I added a new case block on the match-case block in the code which asked the user
to input the todo number to edit which was basically list indexing. The user then had to input another todo to replace the todo the user wanted to edit.
I had to also factor in the fact that python count starts from 0 and human count starts from 1, so I had to deduct 1 from the user number input in the code to cater for both. I run the code after I was done, and it ran as it should have.

I also experimented with the python data types especially strings and list and the appropriate use cases for them. eg a string of 10 is totally different from an integer 10, so you can't do math operations with the string 10. 

There was also a bonus where I used the .replace(__old, __new, Count) methods to replace a particular string in a list of string. Strings are immutable in python, but it's not completely impossible to make changes in a string or mutate. This is where
methods like .replace() comes into play. I used this opportunity to understand why strings are immutable and lists are not. Lists can also be made immutable by transforming them into Tuples.

I did a few more exercises on bug fixing.

Lastly, I learned about the differences between text editors, code editors and IDEs.


Overall, the fourth day was good for me, I learned something new. I will keep building on the to-do app making it more robust in the coming days.