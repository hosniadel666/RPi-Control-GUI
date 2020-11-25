#import RPi.GPIO as GPIO
from GUI import window
class Control(window):

    PIR = 15
    PIN_SERVOPWM = 11
    PIN_FANPWM = 5
    PIN_LEDPWM = 7
    PIN_ROOM = 13
    ROOM_STATE = 0
    SENSOR_SIGNAL = 0  

    def __init__(self):
        print(".............................................................>>>>>>>>>>>>>>>>>>")
        # GPIO configuration
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.led_init()
        self.fan_init()
        self.servo_init()
        self.room_init()
        
    def led_init(self):
        # LED intensity
        GPIO.setup(self.PIN_LEDPWM, GPIO.OUT)
        self.led_intensity = GPIO.PWM(self.PIN_LEDPWM, 100)
        self.led_intensity.start(0)
        
    def fan_init(self):
        # Control fan speed
        GPIO.setup(self.PIN_FANPWM, GPIO.OUT)
        self.fan_speed = GPIO.PWM(self.PIN_FANPWM, 25000)
        self.fan_speed.start(0)
        
    def servo_init(self):   
        # Control the servo angle
        GPIO.setup(self.PIN_SERVOPWM, GPIO.OUT)
        self.servo_pwm = GPIO.PWM(self.PIN_SERVOPWM,50)
        self.servo_pwm.start(2)
        
    def room_init(self):
        # Controle the light of the roon
        GPIO.setup(self.PIN_ROOM, GPIO.OUT)
        GPIO.output(self.PIN_ROOM, True)
    def pir_init(self):
        # PIR sensor
        GPIO.setup(self.PIR, GPIO.IN)
    
    # Room functionality        
    def turn_on(self):
        self.ROOM_STATE = 1
        GPIO.output(self.PIN_ROOM,False)
        self.room_state.value = "ON"
        self.room_state.text_color = (0, 153, 0)
            

    def turn_off(self):
        self.ROOM_STATE = 0
        GPIO.output(self.PIN_ROOM,True)
        self.room_state.value = "OFF"
        self.room_state.text_color =  (102, 0, 51)
            

    # Servo motor rotation
    def servo_rotate():
        angle_val = float(servo_angle.value)
        if angle_val < 0 or angle_val > 180:
            app.error("error","put angle between 0-180")
        else:
            #servo_pwm.ChangeDutyCycle ( (1.0/18.0 * angle_val) + 2)
            servo_angle.value = ""
            
    def servo_rotate_zero():
        #servo_pwm.ChangeDutyCycle ( (1/18.0 * 0) + 2)
        print("hi")
        
    def servo_rotate_90():
        #servo_pwm.ChangeDutyCycle ( (1/18.0 * 90) + 2)
        print("hi")
        
    def servo_rotate_180():
        #servo_pwm.ChangeDutyCycle ( (1/18.0 * 180) + 2)
        print("hi")
        

            
    # Write a message to LCD
    def display_on_lcd():
        if lcd_text_box.value != "":
            app.info("LCD Display", lcd_text_box.value)
            lcd_text_box.value = ""
        #text_box.value = "Display button is pressed"

    def get_folder():
        path.value = app.select_folder()

    def PIR_detect():
        global pir_mail_counter, session
        # text_box3.value = reading
        '''
        if GPIO.input(PIR) == 1 :
            PIR_reading_text.value = "True"
            PIR_reading_text.text_color = (0, 153, 0)
            if pir_mail_counter == 0:
                send_mail(PIR_mail)
                pir_mail_counter += 1
                

        else:
            PIR_reading_text.value = "False"
            PIR_reading_text.text_color = (102, 0, 51)

        '''
    def sound_detect():
     
        # self.text_box3.value = reading
        if self.SENSOR_SIGNAL== 0:
            self.sound_reading_text.value = "False"
            self.sound_reading_text.text_color = (102, 0, 51)
        else:
            self.sound_reading_text.value = "False"
            #sound_reading_text.text_color = (0, 153, 0)
        
    def flame_detect():

        # self.text_box3.value = reading
        if SENSOR_SIGNAL== 0:
            self.falme_reading_text.value = "False"
            self.falme_reading_text.text_color = (102, 0, 51)
        else:
            self.falme_reading_text.value = "False"
            #falme_reading_text.text_color = (0, 153, 0)
            #soundChannelA.play(warning_tone[
            
    def ultrasonic_measure():
        
        # text_box3.value = reading
        self.ultrasonic_reading_text.value = "Distance = " + str(SENSOR_SIGNAL) + " cm"
        
    def LED_intensity_control(Duty):
        #led_intensity.ChangeDutyCycle(int(Duty))
        self.text2.value = "D of LED = " + Duty + " %"

    def fan_speed_control(Duty):
        #fan_speed.ChangeDutyCycle(int(Duty))
        self.fan_speed_display.value = "D of Fan = " + Duty + " %"
        