"""
Created on Wen Aug 13 2020

@author: Hosni Adel
"""

#import pygame.mixer
from time import sleep
from guizero import App,Picture, Text, Slider, TextBox, PushButton, Window, Box,MenuBar
from sys import exit
#import RPi.GPIO as GPIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PIR_mail = "Hosni there is some one here, The PIR detect a motion"
PIR = 15
PIN_SERVOPWM = 11
PIN_FANPWM = 5
PIN_LEDPWM = 7
PIN_ROOM = 13
ROOM_STATE = 0
SENSOR_SIGNAL = 0  
music_index = 0
pir_mail_counter = 0



def send_mail(mail_body):
    # The mail addresses and password
    sender_address = 'xxxxxxxxxxxxxxxxxxxxxx'
    sender_pass = 'xxxxxxxxxxxxx'
    receiver_address = 'xxxxxxxxxxxxxxxxx' 

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "Attention !"

    mail_content = mail_body
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    
def start_music():
    soundChannelA.play(music_list[0])
    
def pause_music():
    pygame.mixer.pause()
def continue_music():
    pygame.mixer.unpause()

def next_music():
    global music_index
    global SENSOR_SIGNAL
    SENSOR_SIGNAL+= 1
    music_index += 1
    soundChannelA.play(music_list[music_index])

def previous_music():
    global SENSOR_SIGNAL
    SENSOR_SIGNAL-= 1
    soundChannelA.play(music_list[SENSOR_SIGNAL])  
    
def music_volume(x):
    soundChannelA.set_volume(float(x) / 100.0)
    
def music_window():
    window = Window(app, title="Music setting")
    window.bg = (156, 153, 153)
    Play = PushButton(window, text = "Play",command=start_music, width = "fill")
    Pause = PushButton(window, text = "Pause", command=pause_music, width = "fill")
    Continue = PushButton(window, text = "Continue", command=continue_music, width = "fill")
    next_ = PushButton(window, text = "next", command=next_music, width = "fill")
    previous = PushButton(window, text = "previous", command=previous_music, width = "fill")
    text_slider = Text(window, text="volume", width = "fill")
    music_volume = Slider(window, command = volume, width = "fill")
    
# Servo motor rotation
def servo_rotate():
    angle_val = float(servo_angle.value)
    if angle_val < 0 or angle_val > 180:
        app.error("error","put angle between 0-180")
    else:
        servo_pwm.ChangeDutyCycle ( (1.0/18.0 * angle_val) + 2)
    servo_angle.value = ""
        
def servo_rotate_zero():
    servo_pwm.ChangeDutyCycle ( (1/18.0 * 0) + 2)
    
def servo_rotate_90():
    servo_pwm.ChangeDutyCycle ( (1/18.0 * 90) + 2)
    
def servo_rotate_180():
    servo_pwm.ChangeDutyCycle ( (1/18.0 * 180) + 2)
    
# Room functionality        
def turn_on():
    global ROOM_STATE
    ROOM_STATE = 1
    GPIO.output(13,False)
    room_state.value = "ON"
    room_state.text_color = (0, 153, 0)
        

def turn_off():
    global ROOM_STATE
    ROOM_STATE = 0
    GPIO.output(13,True)
    room_state.value = "OFF"
    room_state.text_color =  (102, 0, 51)
        
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
    if GPIO.input(PIR) == 1 :
        PIR_reading_text.value = "True"
        PIR_reading_text.text_color = (0, 153, 0)
        if pir_mail_counter == 0:
            send_mail(PIR_mail)
            pir_mail_counter += 1
            

    else:
        PIR_reading_text.value = "False"
        PIR_reading_text.text_color = (102, 0, 51)


def sound_detect():
    global SENSOR_SIGNAL
    # text_box3.value = reading
    if SENSOR_SIGNAL== 0:
        sound_reading_text.value = "False"
        sound_reading_text.text_color = (102, 0, 51)
    else:
        sound_reading_text.value = "False"
        #sound_reading_text.text_color = (0, 153, 0)
    
def flame_detect():
    global SENSOR_SIGNAL
    # text_box3.value = reading
    if SENSOR_SIGNAL== 0:
        falme_reading_text.value = "False"
        falme_reading_text.text_color = (102, 0, 51)
    else:
        falme_reading_text.value = "False"
        #falme_reading_text.text_color = (0, 153, 0)
        #soundChannelA.play(warning_tone[
        
def ultrasonic_measure():
    global SENSOR_SIGNAL
    # text_box3.value = reading
    ultrasonic_reading_text.value = "Distance = " + str(SENSOR_SIGNAL) + " cm"
    
def LED_intensity_control(Duty):
    led_intensity.ChangeDutyCycle(int(Duty))
    text2.value = "D of LED = " + Duty + " %"

def fan_speed_control(Duty):
    fan_speed.ChangeDutyCycle(int(Duty))
    fan_speed_display.value = "D of Fan = " + Duty + " %"
    
def full_screen():
    app.full_screen = True
    
def normal_screen():
    app.full_screen = False

def exit_app():
    app.destroy()
    GPIO.cleanup()
    fan_speed.ChangeDutyCycle(0)

#def init_control:

    '''
    # GPIO configuration
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # LED intensity
    GPIO.setup(PIN_LEDPWM, GPIO.OUT)
    led_intensity = GPIO.PWM(PIN_LEDPWM, 100)
    led_intensity.start(0)

    # Control fan speed
    GPIO.setup(PIN_FANPWM, GPIO.OUT)
    fan_speed = GPIO.PWM(PIN_FANPWM, 25000)
    fan_speed.start(0)

    # Control the servo angle
    GPIO.setup(PIN_SERVOPWM, GPIO.OUT)
    servo_pwm = GPIO.PWM(PIN_SERVOPWM,50)
    servo_pwm.start(2)

    # Controle the light of the roon
    GPIO.setup(PIN_ROOM, GPIO.OUT)
    GPIO.output(PIN_ROOM, True)

    # PIR sensor
    GPIO.setup(PIR, GPIO.IN)




# Chanal configuration for Music
pygame.mixer.init(48000, -16, 1, 1024)

warning_tones = []
warning_tones.append(pygame.mixer.Sound("/home/pi/Desktop/music/3-tspt_danger_alarm_loop_024.wav"))
warning_tones.append(pygame.mixer.Sound("/home/pi/Desktop/music/4-zapsplat_emergency_siren_air_raid_synthesized.wav"))
warning_tones.append(pygame.mixer.Sound("/home/pi/Desktop/music/1-zapsplat_emergency_siren_alarm_serious_harsh_42790.wav"))
warning_tones.append(pygame.mixer.Sound("/home/pi/Desktop/music/2-zapsplat_emergency_alarm_siren_small_digital_beeps_fast_39924.wav"))

music_list = []
music_list.append(pygame.mixer.Sound("/home/pi/Desktop/music/Bent_El_Giran_Melody4Arab.Com.wav") )
music_list.append(pygame.mixer.Sound("/home/pi/Desktop/music/ya_bent_alpy.wav"))
music_list.append(pygame.mixer.Sound("/home/pi/Desktop/music/Kaab_El_Gazal_Melody4Arab.Com.wav"))


soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
'''
def h():
    app = App(width = 800, height = 800, title = "my first GUI")
    app.bg = (156, 153, 153)
    init_control()

    # menu bar
    menubar = MenuBar(app,
                      toplevel = ["File", "view"],
                      options = [
                          [ ["music", music_window] , ["Exit", exit_app]],
                          [ ["full-screen", full_screen], ["normal screen", normal_screen]]
                      ])
    name_box = Box(app, border = 1, width = "fill")
    Text(name_box, font = "Times New Roman", text = "Hosni RPi-GUI-App", width = "fill", color = (0,0,128))
    # win of music
    Text(app, font = "Times New Roman", text = "Music", width = "fill", color = (145, 15, 15))
    music_box1 = Box(app, border = 1, width = "fill")
    music_window_button = PushButton(music_box1, align = "left", text = "Music", command = music_window) #, image = "/home/pi/Desktop/music/download.png")
    music_volume_slider = Slider(music_box1,start = 100, end = 0 , command = music_volume, height = "fill" , width = 20, horizontal = False, align = "left")
    music_box2 = Box(music_box1,align = "left", width = "fill")
    music_play_button = PushButton(music_box2, text = "Play", command = start_music, width = "fill")
    music_pause_button = PushButton(music_box2, text = "Pause", command = pause_music, width = "fill")
    music_continue_button = PushButton(music_box2, text = "Continue", command = continue_music, width = "fill")
    music_next_button = PushButton(music_box2, text = "next", command = next_music, width = "fill")
    music_previous_button = PushButton(music_box2, text = "previous", command = previous_music, width = "fill")
    #box3 = Box(box1,align = "left", width = "fill")
    #music_volume = Slider(box3,start = 100, end = 0 ,command = volume, height = 200, horizontal = False, align = "left")



    # led intensity
    text_ledpwm = Text(app, font = "Times New Roman", text="LED intensity", width = "fill", color = (145, 15, 15))
    box4 = Box(app, border = 1, width = "fill")
    LEDPwm = Slider(box4, command = LED_intensity_control, width = "fill",align = "left")
    LEDPwm.bg = (255, 255, 255)
    text2 = Text(box4, text = "D of LED = 0 %",align = "left")
    text2.text_color = (0,0,128)



    # Fan speed
    fan_speed_text = Text(app, font = "Times New Roman", text="Fan speed", width = "fill", color = (145, 15, 15))
    fan_speed_box = Box(app, border = 1, width = "fill")
    fan_speed_slider = Slider(fan_speed_box, command = fan_speed_control, width = "fill", align = "left")
    fan_speed_slider.bg = (255, 255, 255)
    fan_speed_display = Text(fan_speed_box, text = "D of fan= 0 %", align = "left")
    fan_speed_display.text_color = (0,0,128)



    # Ddisplay on lcd
    lcd_text = Text(app, font = "Times New Roman",text="LCD", color = (145, 15, 15))
    lcd_box = Box(app, border = 1, width = "fill")
    lcd_text_box = TextBox(lcd_box, width = "fill", align = "left")
    disply_lcd = PushButton(lcd_box, text="Display", command = display_on_lcd, align = "left")
    lcd_text_box.bg = (255, 255, 255)
    lcd_text_box.text_size = 15



    # Servo motor
    servo_text = Text(app, font = "Times New Roman", text="Servo angle", width = "fill", color = (145, 15, 15))
    servo_box1 = Box(app, border = 1, width = "fill")
    servo_angle = TextBox(servo_box1, width = "fill", align = "left")
    rotate = PushButton(servo_box1, text = "Rotate",align = "left", command = servo_rotate)
    servo_box2 = Box(app, border = 1, width = "fill")
    rotate_0 = PushButton(servo_box2, text = "Rotate 0 ", align = "left", width = "fill", command = servo_rotate_zero)
    rotate_90 = PushButton(servo_box2, text = "Rotate 90", align = "left", width = "fill", command = servo_rotate_90)
    rotate_180 = PushButton(servo_box2, text = "Rotate180", align = "left", width = "fill", command = servo_rotate_180)
    servo_angle.bg = (255, 255, 255)
    servo_angle.text_size = 15



    # Control room light
    room_text = Text(app, font = "Times New Roman", text = "Room Light", width = "fill", color = (145, 15, 15))
    room_box = Box(app, border = 1, width = "fill")
    room_turnon = PushButton(room_box, text="Turn on", width = "fill", command = turn_on, align = "left")
    room_turnoff = PushButton(room_box, text="Turn off", width = "fill", command = turn_off, align = "left")
    room_state = Text(room_box, align = "left")
    room_state.value = "OFF"
    room_state.text_color =  (102, 0, 51)

    Text(app)

    # Box which group the four boxes
    sensors_box = Box(app, width = "fill")

    # display ultrasonic reading
    ultrasonic_box = Box(sensors_box, border = 1, width = "fill", align = "left")
    ultrasonic_text = Text(ultrasonic_box, font = "Times New Roman", text="Ultrasonic Reading", width = "fill", color = (145, 15, 15))
    ultrasonic_reading_text = Text(ultrasonic_box, text = "the Distance = 0 CM")
    ultrasonic_reading_text.repeat(200, ultrasonic_measure)


    # PIR object Detection
    PIR_box = Box(sensors_box, border = 1, width = "fill", align = "left")
    PIR_text = Text(PIR_box, font = "Times New Roman", text="Object Detection", width = "fill", color = (145, 15, 15))
    PIR_reading_text = Text(PIR_box)
    PIR_reading_text.repeat(150, PIR_detect)

    # Sound sensor
    sound_box = Box(sensors_box, border = 1, width = "fill", align = "left")
    sound_text = Text(sound_box, font = "Times New Roman", text="Sound Detection", width = "fill", color = (145, 15, 15))
    sound_reading_text = Text(sound_box)
    sound_reading_text.repeat(200, sound_detect)


    # flame sensor
    flame_box = Box(sensors_box, border = 1, width = "fill", align = "left")
    flame_text = Text(flame_box, font = "Times New Roman", text="Flame Detection", width = "fill", color = (145, 15, 15))
    falme_reading_text = Text(flame_box)
    falme_reading_text.repeat(200, flame_detect)


    app.display()
def main():
    h()


if __name__ == "__main__":
    main()