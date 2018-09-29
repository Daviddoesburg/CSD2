import simpleaudio as sa
import wave

wave_read = wave.open("/Users/Daviddoesburg/Documents/CSD2/python_basics/Hat_Closed_05.wav", 'rb')
audio_data = wave_read.readframes(wave_read.getnframes())
num_channels = wave_read.getnchannels()
bytes_per_sample = wave_read.getsampwidth()
sample_rate = wave_read.getframerate()






import simpleaudio as sa

print("how many times do you want to hear the sample")



# wave_obj = sa.WaveObject.from_wave_file("/Users/Daviddoesburg/Documents/CSD2/python_basics/Hat_Closed_05.wav")

 
amount = int(input())

for i in range(amount):

	play_obj = sa.play_buffer(audio_data, num_channels, bytes_per_sample, sample_rate)
	play_obj.wait_done()

#	play_obj = wave_obj.play()
#	play_obj.wait_done()
