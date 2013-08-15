## Introduction to Raspberry Pi
### Matt Nodurfth



## Raspberry Pi Computer
* Cheap, $35 USD
* Powerful
* Linux
* Easy to use with existing parts
* GPIO Pins



## What can be done with a Raspberry Pi?


## RaspBMC



## Home automation



## Education!




## Linux
We're using Raspbian, but there are many flavors!


## OK, Let's get started
* User: `pi`
* Password: `raspberry`


What can you see?


###Let's ...
See where we are:
    
    pwd
Look at current directory

    ls
Make a directory
    
    mkdir  MakerFaire
Move around
    
    cd MakerFaire
Make a file
    
    touch filename.py


##  Ok, time for the safety of the GUI
    startx




## Let's build this simple circuit
* Connect:
  * Vcc to pin 3.3V
  * Ground to GND
  * Input Pin to pin 25

![Pullup Resistor](images/pullup.png)



## Let's Look at Code!
* Python to make a game!
* RPi.GPIO and stopwatch modules
* Five Second Stadium



## Let's Play!
    sudo python ffs.py



## What's the problem with our current design?



## Switch Bounce
![Taken from www.ikalogic.com](images/debounceCircuit.jpg)
