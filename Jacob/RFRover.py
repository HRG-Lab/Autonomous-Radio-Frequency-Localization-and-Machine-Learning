#!/usr/bin/python3
# Filename: MultiprocessingPing.py
# >>Designed for Python 3

# --Reads data from two HC-SR04 Ultrasonic Sensors to determine
# --the location of an object between them. The program will send
# --movement commands to a Pixhawk controller that is serially
# --connected to a raspberry pi via MavLink protocol based on the
# --position of the object between the two sensors.

from dronekit import connect, VehicleMode
import time
import multiprocessing as mp
import RPi.GPIO as GPIO
from pymavlink import mavutil
#--- Start the Software In The Loop (SITL)
import dronekit_sitl

def ping(TRIG, ECHO):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    
    GPIO.output(TRIG, False)
    time.sleep(3)           #Waiting for sensor to settle

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
                
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
                   
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    GPIO.cleanup()
    return distance

def vehicle_param():
    sitl = dronekit_sitl.start_default()   #(sitl.start)
    connection_string = "dev/ttyAMA0"
    baud_rate = 115200
    #--- Now that we have started the SITL and we have the connection string (basically the ip and udp port)...
    print(">>>> Connecting with the UAV <<<")
    vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)     #- wait_ready flag hold the program untill all the parameters are been read (=, not .)
    
    #-- Read information from the autopilot:
    #- Version and attributes
    vehicle.wait_ready('autopilot_version')
    print('Autopilot version: %s'%vehicle.version)
    #- Does the firmware support the companion pc to set the attitude?
    print('Supports set attitude from companion: %s'%vehicle.capabilities.set_attitude_target_local_ned)
    #- Read the actual position
    print('Position: %s'% vehicle.location.global_relative_frame)
    #- Read the actual attitude roll, pitch, yaw
    print('Attitude: %s'% vehicle.attitude)
    #- Read the actual velocity (m/s)
    print('Velocity: %s'%vehicle.velocity) #- North, east, down
    #- When did we receive the last heartbeat
    print('Last Heartbeat: %s'%vehicle.last_heartbeat)
    #- Is the vehicle good to Arm?
    print('Is the vehicle armable: %s'%vehicle.is_armable)
    #- Which is the total ground speed?   Note: this is settable
    print('Groundspeed: %s'% vehicle.groundspeed) #(%)
    #- What is the actual flight mode?    Note: this is settable
    print('Mode: %s'% vehicle.mode.name)
    #- Is the vehicle armed               Note: this is settable
    print('Armed: %s'%vehicle.armed)
    #- Is thestate estimation filter ok?
    print('EKF Ok: %s'%vehicle.ekf_ok)

def measure(d, n, trig, echo):   #d=the gloab distance variale shared between processes, n=the sensor number, trig and echo reference the GPI pins that the ping sensor utilizes.
    while True:
        d.value=ping(trig, echo)
        print ('Sensor',n,'output:',d.value,'cm')

def location(d1, d2, destination):
    while True:
        time.sleep(3.0036)             #0.0018s is added to compensate for the difference in time to execute measure vs location.
        tot_dist=d1.value+d2.value     # the total distance based on current measurements.
        loc=abs(tot_dist-d1.value)     # the approximate location of the object in centimeters relative to sensor 1
        print ("Destination:",destination,"\nLocation:", loc, "cm.")
        
        if loc-destination > 0.5:             # {If location-destination is less than 0.5 cm
            #MOT_1_DIRECTION(-1)              #  or greater than 0.5cm the rover will move accordingly
            print ("Rover moves backward \n")  #  this is to leave a +-0.5cm error buffer.}
        elif loc-destination < -0.5:   
            #MOT_1_DIRECTION(1)
            print ("Rover moves foreward \n")
        else:
            print("Arrived!")
            p1.terminate()
            p2.terminate()
            exit(1)
            
if __name__ == "__main__":
    destination = 13               #<<<<<<<<<< SPECIFY DESTINATION HERE! <<<<<<<<<<
    dist1=mp.Value('d', 0.0)
    dist2=mp.Value('d', 0.0)
    #vehicle_param()
    
    p1=mp.Process(target=measure, args=(dist1, 1, 23, 24))    #initializing the child process for sensor 1 to measure
    p2=mp.Process(target=measure, args=(dist2, 2, 22, 27))    #initializing the child process for sensor 2 to measure
    p3=mp.Process(target=location, args=(dist1, dist2, destination))      #initializing the child process for the location to be determined
    
    p1.start()           #starting p1
    p2.start()           #starting p2
    time.sleep(0.005)    #an added delay to synchronize the child processes. 0.0036s is added to compensate for the initial execution delay of p1 and p2.
    p3.start()           #starting p3
    
    p1.join()   #limiting p1 to timeout in 10s
    p2.join()   #limiting p2 to timeout in 10s
    p3.join()   #limiting p3 to timeout in 10s
    
    print("Done!")
    
