#from ctl import control

from time import sleep
from guizero import App,Picture, Text, Slider, TextBox, PushButton, Window, Box,MenuBar
from sys import exit

class window:
    def __init__(self):
        control = Control()
        music = Music()
        notification = Notification()

        app = App(width = 800, height = 800, title = "my first GUI")
        app.bg = (156, 153, 153)

        # menu bar
        menubar = MenuBar(app,
                          toplevel = ["File", "view"],
                          options = [
                              [ ["music", self.music_window] , ["Exit", self.exit_app]],
                              [ ["full-screen", self.full_screen], ["normal screen", self.normal_screen]]
                          ])
        name_box = Box(app, border = 1, width = "fill")
        Text(name_box, font = "Times New Roman", text = "Hosni RPi-GUI-App", width = "fill", color = (0,0,128))
        # win of music
        Text(app, font = "Times New Roman", text = "Music", width = "fill", color = (145, 15, 15))
        music_box1 = Box(app, border = 1, width = "fill")
        music_window_button = PushButton(music_box1, align = "left", text = "Music", command = self.music_window) #, image = "/home/pi/Desktop/music/download.png")
        music_volume_slider = Slider(music_box1,start = 100, end = 0 , command = self.music_volume, height = "fill" , width = 20, horizontal = False, align = "left")
        music_box2 = Box(music_box1,align = "left", width = "fill")
        music_play_button = PushButton(music_box2, text = "Play", command = self.music.start_music, width = "fill")
        music_pause_button = PushButton(music_box2, text = "Pause", command = self.music.pause_music, width = "fill")
        music_continue_button = PushButton(music_box2, text = "Continue", command = self.music.continue_music, width = "fill")
        music_next_button = PushButton(music_box2, text = "next", command = self.music.next_music, width = "fill")
        music_previous_button = PushButton(music_box2, text = "previous", command = self.music.previous_music, width = "fill")
        #box3 = Box(box1,align = "left", width = "fill")
        #music_volume = Slider(box3,start = 100, end = 0 ,command = volume, height = 200, horizontal = False, align = "left")



        # led intensity
        text_ledpwm = Text(app, font = "Times New Roman", text="LED intensity", width = "fill", color = (145, 15, 15))
        box4 = Box(app, border = 1, width = "fill")
        LEDPwm = Slider(box4, command = self.control.LED_intensity_control, width = "fill",align = "left")
        LEDPwm.bg = (255, 255, 255)
        text2 = Text(box4, text = "D of LED = 0 %",align = "left")
        text2.text_color = (0,0,128)



        # Fan speed
        fan_speed_text = Text(app, font = "Times New Roman", text="Fan speed", width = "fill", color = (145, 15, 15))
        fan_speed_box = Box(app, border = 1, width = "fill")
        fan_speed_slider = Slider(fan_speed_box, command = self.control.fan_speed_control, width = "fill", align = "left")
        fan_speed_slider.bg = (255, 255, 255)
        fan_speed_display = Text(fan_speed_box, text = "D of fan= 0 %", align = "left")
        fan_speed_display.text_color = (0,0,128)



        # Ddisplay on lcd
        lcd_text = Text(app, font = "Times New Roman",text="LCD", color = (145, 15, 15))
        lcd_box = Box(app, border = 1, width = "fill")
        self.lcd_text_box = TextBox(lcd_box, width = "fill", align = "left")
        disply_lcd = PushButton(lcd_box, text="Display", command = self.control.display_on_lcd, align = "left")
        self.lcd_text_box.bg = (255, 255, 255)
        self.lcd_text_box.text_size = 15



        # Servo motor
        servo_text = Text(app, font = "Times New Roman", text="Servo angle", width = "fill", color = (145, 15, 15))
        servo_box1 = Box(app, border = 1, width = "fill")
        servo_angle = TextBox(servo_box1, width = "fill", align = "left")
        rotate = PushButton(servo_box1, text = "Rotate",align = "left", command = self.control.servo_rotate)
        servo_box2 = Box(app, border = 1, width = "fill")
        rotate_0 = PushButton(servo_box2, text = "Rotate 0 ", align = "left", width = "fill", command = self.control.servo_rotate_zero)
        rotate_90 = PushButton(servo_box2, text = "Rotate 90", align = "left", width = "fill", command = self.control.servo_rotate_90)
        rotate_180 = PushButton(servo_box2, text = "Rotate180", align = "left", width = "fill", command = self.control.servo_rotate_180)
        servo_angle.bg = (255, 255, 255)
        servo_angle.text_size = 15



        # Control room light
        room_text = Text(app, font = "Times New Roman", text = "Room Light", width = "fill", color = (145, 15, 15))
        room_box = Box(app, border = 1, width = "fill")
        room_turnon = PushButton(room_box, text="Turn on", width = "fill", command = self.control.turn_on, align = "left")
        room_turnoff = PushButton(room_box, text="Turn off", width = "fill", command = self.control.turn_off, align = "left")
        self.room_state = Text(room_box, align = "left")
        self.room_state.value = "OFF"
        self.room_state.text_color =  (102, 0, 51)

        Text(app)

        # Box which group the four boxes
        sensors_box = Box(app, width = "fill")

        # display ultrasonic reading
        ultrasonic_box = Box(sensors_box, border = 1, width = "fill", align = "left")
        ultrasonic_text = Text(ultrasonic_box, font = "Times New Roman", text="Ultrasonic Reading", width = "fill", color = (145, 15, 15))
        ultrasonic_reading_text = Text(ultrasonic_box, text = "the Distance = 0 CM")
        ultrasonic_reading_text.repeat(200, self.control.ultrasonic_measure)


        # PIR object Detection
        PIR_box = Box(sensors_box, border = 1, width = "fill", align = "left")
        PIR_text = Text(PIR_box, font = "Times New Roman", text="Object Detection", width = "fill", color = (145, 15, 15))
        self.PIR_reading_text = Text(PIR_box)
        self.PIR_reading_text.repeat(150, self.control.PIR_detect)

        # Sound sensor
        sound_box = Box(sensors_box, border = 1, width = "fill", align = "left")
        sound_text = Text(sound_box, font = "Times New Roman", text="Sound Detection", width = "fill", color = (145, 15, 15))
        sound_reading_text = Text(sound_box)
        sound_reading_text.repeat(200, self.control.sound_detect)


        # flame sensor
        flame_box = Box(sensors_box, border = 1, width = "fill", align = "left")
        flame_text = Text(flame_box, font = "Times New Roman", text="Flame Detection", width = "fill", color = (145, 15, 15))
        falme_reading_text = Text(flame_box)
        falme_reading_text.repeat(200, self.control.flame_detect)
        app.display()
        

        
    def music_window():
        window = Window(app, title="Music setting")
        window.bg = (156, 153, 153)
        Play = PushButton(window, text = "Play",command=self.start_music, width = "fill")
        Pause = PushButton(window, text = "Pause", command=self.pause_music, width = "fill")
        Continue = PushButton(window, text = "Continue", command=self.continue_music, width = "fill")
        next_ = PushButton(window, text = "next", command=self.next_music, width = "fill")
        previous = PushButton(window, text = "previous", command=self.previous_music, width = "fill")
        text_slider = Text(window, text="volume", width = "fill")
        music_volume = Slider(window, command = volume, width = "fill")
        

 
if __name__ == '__main__':
    window()
