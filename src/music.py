import pygame.mixer


class Music(object):
	def __init__():
		pygame.mixer.init(48000, -16, 1, 1024)

		self.warning_tones = []
		self.warning_tones.append(pygame.mixer.Sound("/home/pi/Desktop/music/3-tspt_danger_alarm_loop_024.wav"))
		self.warning_tones.append(pygame.mixer.Sound("/home/pi/Desktop/music/4-zapsplat_emergency_siren_air_raid_synthesized.wav"))
		self.warning_tones.append(pygame.mixer.Sound("/home/pi/Desktop/music/1-zapsplat_emergency_siren_alarm_serious_harsh_42790.wav"))
		self.warning_tones.append(pygame.mixer.Sound("/home/pi/Desktop/music/2-zapsplat_emergency_alarm_siren_small_digital_beeps_fast_39924.wav"))

		self.music_list = []
		self.music_list.append(pygame.mixer.Sound("/home/pi/Desktop/music/Bent_El_Giran_Melody4Arab.Com.wav") )
		self.music_list.append(pygame.mixer.Sound("/home/pi/Desktop/music/ya_bent_alpy.wav"))
		self.music_list.append(pygame.mixer.Sound("/home/pi/Desktop/music/Kaab_El_Gazal_Melody4Arab.Com.wav"))


		self.soundChannelA = pygame.mixer.Channel(1)
		self.soundChannelB = pygame.mixer.Channel(2)
		

	 def start_music():
        self.soundChannelA.play(music_list[0])
        
    def pause_music():
        self.pygame.mixer.pause()
    def continue_music():
        self.pygame.mixer.unpause()

    def next_music():
 
        self.music_index += 1
        self.soundChannelA.play(music_list[music_index])

    def previous_music():

        self.SENSOR_SIGNAL-= 1
        self.soundChannelA.play(music_list[SENSOR_SIGNAL])  
        
    def music_volume(x):
        self.soundChannelA.set_volume(float(x) / 100.0)