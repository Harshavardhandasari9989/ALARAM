import datetime
import time
import os
import random
import subprocess
def convert_to_24_format(time_str):
    try:
        return datetime.datetime.strptime(time_str,"%I:%M:%S %p").strftime("%H:%M:%S")
    except ValueError:
        print("Please enter in HH:MM:SS AM/PM format.")
        exit()
def random_song():
    download_path="/Users/harshavardhandasari/Downloads"
    song=[f for f in os.listdir(download_path) if f.endswith(".mp3")]
    if not song:
        print("No mp3 file Found.")
        return None
    return os.path.join(download_path,random.choice(song))
def set_alaram(alarm_time):
    song=random_song()
    if not song:
        return 
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        if current_time==alarm_time:
            print("\n⏰ Time to Wake Up! Playing Alarm... ⏰")
            process=subprocess.Popen(["afplay",song])
            time.sleep(60)
            process.terminate()
            print("⏹️ Alarm Stopped! ")
            break
        time.sleep(1)
alarm_input_time=input("Enter alarm time in HH:MM:SS AM/PM format : ")
alarm_time=convert_to_24_format(alarm_input_time)
print(f"\nAlarm set for {alarm_input_time} ⏳")
set_alaram(alarm_time)
            
        