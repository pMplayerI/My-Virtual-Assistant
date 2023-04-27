import pyttsx3
import speech_recognition
import pyaudio
import playsound
import os
import webbrowser
from datetime import date, datetime
from gtts import gTTS

def textToSpeech(brain):
    output = gTTS(brain, lang='vi', slow=False)
    output.save("voice.mp3")
    playsound.playsound("voice.mp3", True)
    # Không xóa là lỗi
    os.remove("voice.mp3")

ear = speech_recognition.Recognizer()
mouth = pyttsx3.init()
brain = "Chào mừng quay lại, thưa chủ nhân!"

print("\nRobot: " + brain)
textToSpeech(brain)


while True:
    # Nhớ lại những gì đã nói
    remember = brain 

    with speech_recognition.Microphone() as mic:
        print("Robot: Tôi đang lắng nghe!")

        # Khoảng trễ nhận mic
        ear.pause_threshold = 1

        # Lọc tiếng ồn
        ear.adjust_for_ambient_noise(mic)

        audio = ear.listen(mic)

    print("Robot: ...")

    try:
        you = ear.recognize_google(audio, language = 'vi-VN')
    except:
        you = "..."

    print("You: " + you)

    # Phần AI
    if "tạm biệt" in you:
        brain = "Hẹn gặp lại!\n"
        print ("Robot: " + brain)
        textToSpeech(brain)

        # Kết thúc chương trình
        break

    elif you == "...":
        brain = "Tôi không hiểu!\n"

    elif "chào" in you:
        brain = "Rất vui khi gặp bạn!\n"

    elif "tên" in you: 
        brain = "Tôi là Bảo, một nô lệ của bạn!\n"

    elif "không nghe" in you or "nói lại" in you:
        brain = remember

    elif "nghe" in you:
        brain = "Vâng, tôi vẫn đang lắng nghe!\n"

    elif "tốt" in you or "giỏi" in you or "cảm ơn" in you:
        brain = "Ok baby!\n"
    
    elif "ngày" in you:
        today = date.today()
        brain = today.strftime("Hôm nay là: ngày %d tháng %m năm %Y\n")

    elif "giờ" in you:
        now = datetime.now();
        brain = now.strftime("%H:%M:%S\n")

    elif "Google" in you or "Chrome" in you:
        webbrowser.open("https://www.google.com/", new=1)
        brain = "Google đã được mở!\n"

    elif "YouTube" in you:
        webbrowser.open("https://www.youtube.com", new=1)
        brain = "Youtube đã được mở!\n"

    elif "Facebook" in you:
        webbrowser.open("https://www.facebook.com/", new=1)
        brain = "Facebook đã được mở!\n"

    else:
        brain = "Tôi khỏe cảm ơn còn bạn!\n"

    print ("Robot: " + brain)
    textToSpeech(brain) 