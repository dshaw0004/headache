# Headache programming

After getting inspired from **Brainfuck** I have made a similar programming language **Headache** but simplier than **Brainfuck**

## Why Headache ?

Certainly, this is not going to fuck your brain like **Brainfuck** but it might give you headache.

## What is Headache ?

**Headache** is a useless programming language made as a joke which can not do anything more than printing some text in terminal.
Inspired from **Brainfuck** it also use symbols only to do stuffs.

## Advantages of Headache

- Good for wasting time

## Disadvantages of Headache

- This is useless

- It can only print characters in the terminal, nothing more than that.

## Getting Started with Headache

Firstly, create a file with `.headache` extension.
Now we will write some *headache* code.
But before that let's learn how it work.

### How to write headache code 

Each line act as a separate block of code.
At the beginning of each line a counter initiate at 65 which is the ASCII value of **'A'**. So if we just write `>` and does not do anything it will print **A** in the terminal. 
Now you have to increament or decreament the counter to reach the ASCII code of your desired symbol. 
And to increament or decreament the counter use **`+` or `-`** symbols respectively.
For example, if you want to print **'D'** you have to do this `+++>`

> Remember one important thing, counter will initiate at 65 at the beginning of line so `+` is 66 and `+++++++++++` is 76, i.e. 'B' and 'L' respectively.

Now to print a new line use **`\`**. It will print new line (\n) only.

It is not necessary that you will only output in capital letters, you might want small letters.
You can get small letters by increamenting the counter to 97 first then increamenting it according to your need.
Or you can use **`@`**, it will move your counter to 97.
Then just increament or decreament the counter usually.

Similar to `@` **`^`** will move the counter to 48. 48 is the ASCII code for the number zero (0). 

In case you need to reset the counter back to 65 in the middle of a line then use **`!`**.

Finally for commenting use **`#`**. But as for v0.1.0 it only support single line comment.
Also commenting after some code in the same line is not support.

```
# this is a comment which is supported
+++> 

+++> # this type of comment is not supported yet.
```

Finally **`.`** ( fullstop or period symbol ) stores the counter value of last line.
Use it at the beginning of a line to get back where you have left in the last line.

## How to run a .headache file

### For linux 

#### Download Executable

At First download the executable of the interpreter from the [**releases**](https://github.com/dshaw0004/headache/releases/) section of this repo.
Then you can few different approachs

    1. create a separate folder for headache files and move the interpreter to that folder. Then use can just to `./headache helloworld.headache`. But in this way you can not use the interpreter globally so easily.

    2. Follow the 1st option but add an _alias_ of the path of the interpreter in your **.bashrc** or equivalent file.
    `alias headache=/path/to/headache/interpreter`

    3. Download the executable then move it to `/bin/` directory to access it from every where. You can use `sudo mv headache /bin/` to move the file to `/bin` directory.

Finally you can just run the headache file by doing `headache filename.headache` in your terminal.

#### Build or Run from scratch

The interpreter of headache is made using python and its a single python file. So you can copy the `headache.py` file the repo and
run that python file with an argument of your headache file path. e.g., `python3 headache.py path/to/file.headache`.

Or 

You can just build a binary executable using **pyinstaller** or any other similar library.

## For Windows

There is no executable for Windows you have to run it from the python file.

`python headache.py path/to/file.headache`

## Cheatsheet

- At the beginning of each line a Counter will start at 65 ( A )

- `>` will Output the symbol for the ASCII code of current number

- `\` will print a new line character ('\n')

- `+` will increase the counter by one

- `-` will decrease the counter by one

- `@` will move counter to 97 (a)

- `!` will reset back the counter to 65 ( A )

- `^` will take the counter to 48 ( number zero )

- `#` will comment out the line

- If the line starts with `.` Then it will continue the counter from last line.


## Example

Hello World program in Headache.

```
# Clean, easy to read one character at a line.

# H
+++++++>
# e
@++++>
# l
.+++++++> 
# l
.>
# o
.+++> 
# <space>
^----------------> 
# W
@----------> 
# o
@++++++++++++++>
# r
.+++> 
# l
.------> 
# d
@+++> 
# !
^---------------> 

```
or you can do this.
```
# everything in one line. Messy code.

+++++++>@++++>+++++++>>+++>^---------------->@---------->@++++++++++++++>+++>------>@+++>^---------------> 

```


## End Note

At the end I would like to its a joke. I have made it as a joke. Don't waste your time in this kind of shit.
**And that's it for version 0.1.0 of headache.**
