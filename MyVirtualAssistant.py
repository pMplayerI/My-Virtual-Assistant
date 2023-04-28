import speech_recognition as sr
import os
import webbrowser
import playsound
from gtts import gTTS
from datetime import date, datetime

# Sửa làm chó
suaLamCho = "Bảo"
now = datetime.now()

# Nghe, hiểu và nói
def listen():
    ear = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Robot: Tôi đang lắng nghe!")
        # Lọc tiếng ồn
        ear.adjust_for_ambient_noise(mic)
        audio = ear.listen(mic)
    print("Robot: ...")
    try:
        text = ear.recognize_google(audio, language="vi-VN")
        print("You: " +text)
        return text
    except:
        text = "..."
        print("You: " +text)
        return text
    
def understand():  
    text = listen()
    return text

def speak(brain):
    print("Robot: " +brain+ "\n")
    output = gTTS(brain, lang="vi", slow=False)
    output.save("voice.mp3")
    playsound.playsound("voice.mp3", True)  
    # Không xóa là lỗi
    os.remove("voice.mp3")

# Các chức năng chính
def hello(name):
    dayTime = int(now.strftime("%H"))
    if 6 <= dayTime < 12:
        brain = "Chào bạn " +name+ "! Chúc bạn một buổi sáng tốt lành!"
        speak(brain)
    elif 12 <= dayTime < 18:
        brain = "Chào bạn " +name+ "! Chúc bạn một buổi chiều tốt lành!"
        speak(brain)
    else:
        brain = "Chào bạn " +name+ "! Chúc bạn một buổi tối tốt lành!"
        speak(brain)

def getToday():
    today = date.today()
    brain = today.strftime("Hôm nay là ngày %d tháng %m năm %Y.")
    speak(brain)

def getTime():
    brain = now.strftime("%H:%M:%S")
    speak(brain)

def searching(text):
    search = text.split("kiếm", 1)[1]
    brain = "Đang tìm kiếm!"
    speak(brain)
    url = "https://www.google.com.tr/search?q=" +search
    webbrowser.open(url, new=1)
    brain = "Đã tìm kiếm thành công!"
    speak(brain)

def openWebsite(text):
    # Lấy dấu cách là không tìm được
    search = text.split("mở ", 1)[1]
    brain = "Đang mở trang web!"
    speak(brain)
    url = "https://www." +search
    webbrowser.open(url, new=1)
    brain = "Trang web bạn yêu cầu đã được mở!"
    speak(brain)

def openApp(text):
    if "google" in text or "chrome" in text:
        brain = "Đang mở Google Chrome!"
        speak(brain)
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        brain = "Google Chrome đã được mở!"
        speak(brain)

    elif "code" in text:
        brain = "Đang mở Visual Studio Code!"
        speak(brain)
        # Có cái r đó máy t mới mở được
        os.startfile(r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe")
        brain = "Visual Studio Code đã được mở!"
        speak(brain)

    elif "game" in text:
        brain = "Đang mở LMHT!"
        speak(brain)
        os.startfile("D:\Riot Games\Riot Client\RiotClientServices.exe")
        brain = "Chơi game ít thôi!"
        speak(brain)

    else:
        brain = "404 not found!"
        speak(brain)

# Tán gẫu
def opening(name):
    brain = "Chào bạn " +name+ "!"
    speak(brain)
    brain = "Tôi có thể giúp gì cho bạn?"
    speak(brain)

def stop():
    brain = "Hẹn gặp lại!"
    speak(brain)

def noisy():
    brain = "Tôi không nghe rõ! Bạn có thể nhắc lại được không?"
    speak(brain)

def baoNgu():
    brain = "Tôi là " +suaLamCho+ ", một nô lệ của bạn!"
    speak(brain)

def stillListening():
    brain = "Vâng, tôi vẫn đang lắng nghe!"
    speak(brain)

def compliment():
    brain = "Ok baby!"
    speak(brain)

def nope():
    brain = "Tôi khỏe cảm ơn còn bạn!"
    speak(brain)

# AI
def ai():
    # Mở đầu
    brain = "Xin chào, bạn tên là gì?"
    speak(brain)
    name = understand()
    opening(name)

    while True:
        # Cho chữ thường hết cho dễ
        text = understand().lower()

        # Xử lý các chức năng chính
        if "chào" in text:
            hello(name)
        
        elif "ngày" in text:
            getToday()

        elif "giờ" in text:
            getTime()

        elif "mở" in text:
            if "." in text:
                openWebsite(text)

            elif "tìm kiếm" in text:
                searching(text)

            else:
                openApp(text)   

        # Xử lý tán gẫu
        elif "tạm biệt" in text:
            stop()
            # Ngừng chương trình
            break

        elif text == "...":
            noisy()

        elif "tên" in text: 
            baoNgu()

        elif "nghe" in text:
            stillListening()

        elif "tốt" in text or "giỏi" in text or "cảm ơn" in text:
            compliment()

        # Hỏi gì khó vậy 3
        else:
            nope()

# Chạy chương trình
ai()