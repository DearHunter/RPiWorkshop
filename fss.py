import stopwatch
import RPi.GPIO as GPIO

pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

print "\n***************************************"
print "*** Welcome to Five Second Stadium! ***"
print "***************************************\n"
print "Press the BUTTON to start and press again to stop after 5 sec!"
print "Press ctrl + c to quit"
print "--------------------------------------------------------------\n"

while True:
    print "Start?"
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    t = stopwatch.Timer()
    print "***Started!***\n\n"
    
    print "Stop?"
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    t.stop()
    rounded = "%.2f" % t.elapsed
    print rounded, " seconds!"
    
    if float(rounded) == 5:
        print "*** Congratulations Champion! ***"
    else:
        print "So Close!"
    
    print "Would you like to play again?"
    GPIO.wait_for_edge(pin, GPIO.FALLING)