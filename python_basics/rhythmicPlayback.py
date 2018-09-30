import simpleaudio as sa
import wave as wa
import time


wave_obj = sa.WaveObject.from_wave_file("/Users/Daviddoesburg/Documents/CSD2/python_basics/Hat_Closed_05.wav")

numPlaybackTimes = int(input())

list1 = []

for i in range(numPlaybackTimes):
    x = float(input())
    list1.append(x)

print("complete list:", list1)

bpm = list1[-1]

del list1 [-1]
#
# print("list without bpm:", list1)
#
# print("BPM:", bpm)

for item in list1:  # range(len(list1)):
    print(item)
    play_obj = wave_obj.play()
    time.sleep(item * (60/bpm))











# print(nump)
