# 0x17. Web stack debugging #3
> ## Foundations - System engineering & DevOps ― Web stack debugging


### ps (process status) command

it is used to get the more and detailed information about a specific process or all processes. For example it is used to know whether a particular process is running or not, who is running what process in system, which process is using higher memory or CPU, how long a process is running, etc.

<p align="center"><img src="images/1.PNG" width="700"></p>

### Strace 

Strace is a diagnostic, debugging and instructional userspace utility for Linux. It is used to monitor and tamper with interactions between processes and the Linux kernel, which include system calls, signal deliveries, and changes of process state.

<p align="center"><img src="images/2.PNG" width="700"></p>

<p align="center"><img src="images/3.PNG" width="700"></p>

### debbuging Strace 

When execute cURL 127.0.0.1, strace show error in -1 ENOENT (No such file or directory)

<p align="center"><img src="images/4.PNG" width="700"></p>

### Probleam 

In the folder /var/www/html/wp-includes, the folder class-wp-locale.php is well written
Wordpress use a file wp-settings.php, Include files required for initialization. the file is misspelled.

<p align="center"><img src="images/5.PNG" width="700"></p>

<p align="center"><img src="images/6.PNG" width="700"></p>


