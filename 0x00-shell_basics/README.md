# **Shell, basics**
> ## *Foundations - System engineering & DevOps ― Bash*

![Ält](https://tricksinfo.net/wp-content/uploads/2019/07/images-6-738x405.jpeg)
## General

* What does RTFM mean?
* What is a Shebang

## What is the Shell

* What is the shell
* What is the difference between a terminal and a shell
* What is the shell prompt
* How to use the history (the basics)

## Navigation

* What do the commands or built-ins cd, pwd, ls do
* How to navigate the filesystem
* What are the . and .. directories
* What is the working directory, how to print it and how to change it
* What is the root directory
* What is the home directory, and how to go there
* What is the difference between the root directory and the home directory of the user root
* What are the characteristics of hidden files and how to list them
* What does the command cd - do

## Looking Around

* What do the commands ls, less, file do
* How do you use options and arguments with commands
* Understand the ls long format and how to display it
* [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
* What does the ln command do
* What do you find in the most common/important directories
* What is a symbolic link Visit my [Blog](https://medium.com/@jclopez100/what-is-the-difference-between-a-hard-link-and-a-symbolic-link-310dd9fedcbc)
* What is a hard link. Visit my [Blog](https://medium.com/@jclopez100/what-is-the-difference-between-a-hard-link-and-a-symbolic-link-310dd9fedcbc) 
* What is the difference between a hard link and a symbolic link

## Manipulating Files

* What do the commands cp, mv, rm, mkdir do
* What are wildcards and how do they work
* How to use wildcards
* Working with Commands
* What do type, which, help, man commands do
* What are the different kinds of commands
* What is an alias
* When do you use the command help instead of man

## Reading Man Pages

* How to read a man page
* What are man page sections
* What are the section numbers for User commands, System calls and Library functions

## Keyboard Shortcuts for Bash
* Common shortcuts for Bash

## LTS

** What does LTS mean?
Long Term Support

### What is "the Shell"?

Simply put, the shell is a program that takes commands from the keyboard and gives them to the operating system to perform. In the old days, it was the only user interface available on a Unix-like system such as Linux. Nowadays, we have graphical user interfaces (GUIs) in addition to command line interfaces (CLIs) such as the shell.

On most Linux systems a program called bash (which stands for Bourne Again SHell, an enhanced version of the original Unix shell program, sh, written by Steve Bourne)

### What's a "Terminal?"
It's a program called a terminal emulator. This is a program that opens a window and lets you interact with the shell.

**A shell prompt** that contains your user name and the name of the machine followed by a dollar sign

**A shebang** is the character sequence consisting of the characters number sign and exclamation mark (#!) at the beginning of a script.
**man** - an interface to the on-line reference manuals
       1.   Executable programs or shell commands
       2.   System calls (functions provided by the kernel)
       3.   Library calls (functions within program libraries)
       4.   Special files (usually found in /dev)
       5.   File formats and conventions eg /etc/passwd
       6.   Games
       7.   Miscellaneous  (including  macro  packages and conven‐
           tions), e.g. man(7), groff(7)
       8.   System administration commands (usually only for root)
       9.   Kernel routines [Non standard]

