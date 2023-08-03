import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

trigpin=40
echopin=38
servo=36

GPIO.setup(trigpin,GPIO.OUT)
GPIO.setup(echopin,GPIO.IN)
GPIO.setup(servo,GPIO.OUT)
pwm=GPIO.PWM(servo,100)

try:
    while True:
        
        GPIO.output(trigpin,0)
        time.sleep(0.2)
        GPIO.output(trigpin,1)
        time.sleep(0.4)
        GPIO.output(trigpin,0)
        
        while GPIO.input(echopin)==0:
            starttime=time.time()
            pass
        
        while GPIO.input(echopin)==1:
            endtime=time.time()
            pass
        
        t_time=endtime-starttime
        distance=t_time*17510
        distance=round(distance,2)
        print("Distance in cm is: ",distance)
        time.sleep(0.2)
        
        if distance<=25 and distance>5:
            DC=distance*(-10/21)+(12)
            DC=(round(DC,1))*10
            pwm.start(0)
            pwm.ChangeDutyCycle(DC)
            print("Current Dutycycle as per object distance is:", DC)
            time.sleep(0.2)

        else:
            pwm.stop()
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print('DONE')