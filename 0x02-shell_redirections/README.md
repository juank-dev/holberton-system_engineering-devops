# **0x02. Shell, I/O Redirections and filters**
> ## Foundations - System engineering & DevOps ― Bash

### Shell, I/O Redirection

![Alt](https://programskills.files.wordpress.com/2016/05/stdin-stdout-stderr.png?w=603&h=387)

* What do the commands head, tail, find, wc, sort, uniq, grep, tr do
* How to redirect standard output to a file
* How to get standard input from a file instead of the keyboard
* How to send the output from one program to the input of another program
* How to combine commands and filters with redirections

### Special Characters

* What are special characters
* Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them

### Other Man Pages

* How to display a line of text
* How to concatenate files and print on the standard output
* How to reverse a string
* How to remove sections from each line of files
* What is the /etc/passwd file and what is its format
* What is the /etc/shadow file and what is its format

![Alt](https://geek-university.com/wp-content/images/linux/redirection_symbols.jpg?x67341)

### Standard Output

Most command line programs that display their results do so by sending their results to a facility called standard output. By default, standard output directs its contents to the display. To redirect standard output to a file, the **">"**
Each time the command above is repeated, file_list.txt is overwritten from the beginning with the output of the command ls. If you want the new results to be appended to the file instead, use **">>"**

### Standard Input

Many commands can accept input from a facility called standard input. By default, standard input gets its contents from the keyboard, but like standard output, it can be redirected. To redirect standard input from a file instead of the keyboard, the "<" character

### Pipelines

The most useful and powerful thing you can do with I/O redirection is to connect multiple commands together with what are called pipelines. With pipelines, the standard output of one command is fed into the standard input of another.

### Filters

One kind of program frequently used in pipelines is called filters. Filters take standard input and perform an operation upon it and send the results to standard output. In this way, they can be combined to process information in powerful ways.

