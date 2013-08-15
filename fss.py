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
  try:
    print "Start?"
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    # nah = raw_input()
    # if nah == 'q': break
    t = stopwatch.Timer()
    print "***Started!***\n\n"
    
    print "Stop?"
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    # nah = raw_input()
    # if nah == 'q': break
    t.stop()
    rounded = "%.2f" % t.elapsed
    print rounded, " seconds!"
    if float(rounded) == 5: 
        print "*** Congratulations Champion! ***"
    else:
        print "So Close!"
    
    print "Would you like to play again?"
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    # nah = raw_input()
    # if nah == 'q': break
  except:
    print "Interrupted!"  # This never gets printed...
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

# GPIO.cleanup() # not needed with button version