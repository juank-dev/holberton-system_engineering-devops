# **0x03. Shell, init files, variables and expansions**
> ## Foundations - System engineering & DevOps ― Bash

### Shell Initialization Files

* What are the /etc/profile file and the /etc/profile.d directory
* What is the ~/.bashrc file

### Variables

* What is the difference between a local and a global variable
* What is a reserved variable
* How to create, update and delete shell variables
* What are the roles of the following reserved variables: HOME, PATH, PS1
* What are special parameters
* What is the special parameter $??

### Expansions

![Alt](https://developer.ibm.com/developer/tutorials/l-linux-shells/images/figure2.gif)

* What is expansion and how to use them
* What is the difference between single and double quotes and how to use them properly
* How to do command substitution with $() and backticks

### Shell Arithmetic

![Alt](https://slideplayer.com/slide/5291571/17/images/26/Arithmetic+Operators+Guide+to+UNIX+Using+Linux%2C+Third+Edition.jpg)

* How to perform arithmetic operations with the shell

### The alias Command

* How to create an alias
* How to list aliases
* How to temporarily disable an alias

### Other help pages
* How to execute commands from a file in the current shell

### EXPANSION

Each time you type a command line and press the enter key, bash performs several processes upon the text before it carries out your command. We have seen a couple of cases of how a simple character sequence, for example “*”, can have a lot of meaning to the shell. The process that makes this happen is called expansion. With expansion, you type something and it is expanded into something else before the shell acts upon it. To demonstrate what we mean by this, let's take a look at the echo command. echo is a shell builtin that performs a very simple task. It prints out its text arguments on standard output
