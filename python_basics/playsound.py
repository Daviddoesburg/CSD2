import simpleaudio as sa

wave_obj =
sa.WaveObject.from_wave_file("/Users/Daviddoesburg/Desktop/Puredata_wav_directory/Atmo_Conga_01.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
