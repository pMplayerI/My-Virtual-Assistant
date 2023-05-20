import speech_recognition as sr
import os
import playsound
from gtts import gTTS
from datetime import date, datetime
import webbrowser
import smtplib
import pyjokes
from deep_translator import GoogleTranslator
import requests
import pywhatkit as pwt
import random
import ctypes
from bs4 import BeautifulSoup
import wikipedia

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
        you = ear.recognize_google(audio, language="vi-VN")
    except:
        you = "..."
    print("You: " +you)
    return you
    
def understand():
    # Quá lần nói hợp lệ sẽ bỏ qua chức năng hiện tại (pass)
    for i in range(2):
        brain = listen()
        if brain != "...":
            # Trả về câu nói
            return brain
        elif i < 1:
            speak("Tôi không nghe rõ! Bạn có thể nhắc lại được không?")
    speak("Đã quá lần nói hợp lệ! Tôi sẽ bỏ qua!")
    # Trả về "..."
    return brain

def speak(brain):
    print("Robot: " +brain+ "\n")
    mouth = gTTS(brain, lang="vi", slow=False)
    mouth.save("voice.mp3")
    playsound.playsound("voice.mp3", True)  
    # Không xóa là lỗi
    os.remove("voice.mp3")

# Các chức năng chính
def hello(name):
    dayTime = int(datetime.now().strftime("%H"))
    if 6 <= dayTime < 12:
        speak("Chào " +name+ "! Chúc bạn một buổi sáng tốt lành!")
    elif 12 <= dayTime < 18:
        speak("Chào " +name+ "! Chúc bạn một buổi chiều tốt lành!")
    else:
        speak("Chào " +name+ "! Chúc bạn một buổi tối tốt lành!")

def getToday(): 
    speak(date.today().strftime("Hôm nay là ngày %d tháng %m năm %Y."))

def getTime():
    speak(datetime.now().strftime("%H:%M:%S"))

def searching():
    speak("Bạn muốn tìm kiếm gì?")
    search = understand()
    if search == "...":
        pass
    else:
        speak("Đang tìm kiếm kết quả!")
        url = "https://www.google.com/search?q=" +search
        webbrowser.open(url, new=1)
        speak("Đã tìm kiếm thành công!")    

def openWebsite():
    speak("Bạn muốn truy cập trang web nào?")
    search = understand()
    if search == "...":
        pass
    else:
        if "." in search:
            speak("Đang truy cập trang web!")
            url = "https://www." +search
            webbrowser.open(url, new=1)
            speak("Trang web bạn yêu cầu đã được truy cập!")
        else:
            speak("Đường dẫn của trang web không hợp lệ!")

def openApp():
    speak("Bạn muốn mở ứng dụng nào?")
    search = understand().lower()
    if search == "...":
        pass
    else:
        if "google" in search or "chrome" in search:
            speak("Đang mở Google Chrome!")
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            speak("Google Chrome đã được mở!")

        elif "code" in search:
            speak("Đang mở Visual Studio Code!")
            os.startfile(r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            speak("Visual Studio Code đã được mở!")

        elif "game" in search:
            speak("Đang mở LMHT!")
            os.startfile("D:\Riot Games\Riot Client\RiotClientServices.exe")
            speak("Chơi game ít thôi!")

        elif "notepad" in search:
            speak("Đang mở Notepad!")
            os.startfile(r"C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad")
            speak("Notepad đã được mở!")

        else:
            speak("Không tìm thấy ứng dụng!")

def playSong():
    speak("Bạn muốn nghe gì?")
    song = understand()
    if song == "...":
        pass   
    else:
        speak("Đang tìm kiếm bài hát!")
        pwt.playonyt(song)
        speak("Bài hát bạn yêu cầu đã được mở!")

def sendEmail():
    sender = "primegaming737@gmail.com"
    # Đây là mật khẩu ứng dụng
    password = "cklylijydznawvwf"

    speak("Bạn muốn gửi email đến ai?")
    receiver = understand().lower().strip()
    if receiver == "...":
        pass  
    else:
        speak("Bạn muốn gửi email đến tên miền nào?")
        domain = understand().lower().strip()
        if domain == "...":
            pass
        else:
            if "." in domain:
                speak("Nội dung của email là gì?")
                content = understand()
                if content == "...":
                    pass
                else:
                    try:
                        message = "Subject: %s\n\n%s"%("Email tự động", content)
                        speak("Email đang được gửi!")
                        session = smtplib.SMTP("smtp.gmail.com", 587)
                        # Xác minh email với smtp gmail client
                        session.ehlo()
                        # Bảo mật email với tls encryption
                        session.starttls()
                        session.login(sender, password)  
                        session.sendmail(sender, receiver.strip() +"@"+ domain.strip(), message.encode("utf-8"))
                        session.close()
                        speak("Đã gửi email thành công!")
                    except:
                        speak("Gửi email không thành công: Email này không tồn tại!")
            else:
                speak("Gửi email không thành công: Tên miền không hợp lệ!")

def weather():
    speak("Bạn muốn xem thời tiết ở địa điểm nào?")
    city = understand()
    if city == "...":
        pass
    else:
        speak("Đang tìm kiếm kết quả!")
        url = "http://api.openweathermap.org/data/2.5/weather?appid=fe8d8c65cf345889139d8e545f57819a&q=" +city+ "&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_temperature = city_res["temp"]
            current_pressure = city_res["pressure"]
            current_humidity = city_res["humidity"]

            suntime = data["sys"]
            sunrise = datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.fromtimestamp(suntime["sunset"])

            wthr = data["weather"]
            weather_description = wthr[0]["description"]               
            speak("\nHôm nay ở " +city+ " sẽ có " +GoogleTranslator(source="auto", target="vi").translate(weather_description)+ "\nMặt trời mọc vào lúc " +str(sunrise.hour)+ " giờ " +str(sunrise.minute)+ " phút\nMặt trời lặn vào lúc " +str(sunset.hour)+ " giờ " +str(sunset.minute)+ " phút\nNhiệt độ trung bình là " +str(current_temperature)+ " độ C\nÁp suất không khí là " +str(current_pressure)+ " Pa\nĐộ ẩm là " +str(current_humidity)+ "%")
        else:
            speak("Không tìm thấy địa điểm của bạn!")

def wallpaper():
    speak("Bạn muốn thay đổi hình nền theo chủ đề gì?")
    query = understand()
    if query == "...":
        pass
    else:
        # Tìm hình nền theo tiếng Anh
        theme = GoogleTranslator(source="auto", target="en").translate(query)
        speak("Đang thay đổi hình nền!")
        try:
            url = "https://api.pexels.com/v1/search?per_page=1&page=" +str(random.randint(1,99))+ "&query=" +theme
            # Cái headers là nó xác thực cái api key
            res = requests.get(url, headers={"Authorization": "IcYG6vQolq3GauSW2Y1DSB95fiIEajpP3zBaf0ocXSb5XIYwJNzBmka3"}) 
            if res.status_code == 200:
                # Lấy url của hình từ response của trang web
                img_url = res.json().get("photos")[0]["src"]["original"]
                # Tạo request để lấy hình
                img = requests.get(img_url)
                # Tải và lưu ảnh về ở C:\Users\Admin
                # Cái wb là chế độ khi tải cái mới thì nó sẽ thay thế cái cũ
                with open("temp.jpg", "wb") as image:
                    image.write(img.content)
            # Cái này để thay đổi hình nền của máy
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd()+"\\temp.jpg", 0)
            speak("Hình nền đã được thay đổi!")
        except:
            speak("Thay đổi hình nền không thành công!")

def newspaper():
    speak("Bạn muốn nghe tin tức theo chủ đề gì?")
    keyword = understand()
    if keyword == "...":
        pass
    else:
        speak("Đang tìm kiếm mẫu tin mới nhất!")
        try:
            response = requests.get("https://tuoitre.vn/tim-kiem.htm?keywords=" +keyword)
            soup = BeautifulSoup(response.content, "html.parser")
            link = soup.find("a",{"class":"box-category-link-title"}).get("href")
            news = requests.get("https://tuoitre.vn" +link)

            soup = BeautifulSoup(news.content, "html.parser")
            title = soup.find("h1", class_="article-title").text.strip()
            description = soup.find("h2", class_="detail-sapo").text.strip()
            body = soup.find("div", class_="detail-cmain")

            speak(title)
            speak(description)   
            for content in body.find_all("p"):
                speak(content.text.strip())
        except:
            speak("Không tìm thấy chủ đề hoặc tin phù hợp!")

def wiki():
    speak("Bạn muốn biết về gì?")
    search = understand()
    if search == "...":
        pass
    else:
        speak("Đang tìm kiếm kết quả!")
        try:
            content = wikipedia.summary(search)
            speak(GoogleTranslator(source="auto", target="vi").translate(content))
        except:
            speak("Tôi không thể định nghĩa được thuật ngữ này!")

# AI
def ai(name):
    thucthi = True
    name =  str(name[0][1])
    speak("Chào " +name+ "! Tôi có thể giúp gì cho bạn?")
    while thucthi == True:
        # Cho chữ thường hết cho dễ
        text = understand().lower()
            
        if "..." in text or "tạm biệt" in text:
            # Ngừng chương trình nếu đang không thực hiện chức năng gì
            speak("Hẹn gặp lại!")
            thucthi = False
            break

        elif "chào" in text:
            hello(name)
            
        elif "ngày" in text:
            getToday()

        elif "giờ" in text:
            getTime()

        elif "tìm kiếm" in text:
            searching()

        elif "truy cập" in text:
            openWebsite()                    

        elif "ứng dụng" in text:
            openApp()                  

        elif "nhạc" in text:
            playSong()                 
                
        elif "mail" in text:
            sendEmail()                 

        elif "thời tiết" in text:
            weather()
                    
        elif "nền" in text:
            wallpaper()
                    
        elif "báo" in text or "tin tức" in text:
            newspaper()                 

        elif "định nghĩa" in text or "giải thích" in text or "wiki" in text:
            wiki()
                    
        # Xử lý tán gẫu
        elif "giúp" in text or "chức năng" in text:
            speak("""Tôi có thể giúp bạn thực hiện các việc sau đây:
            1. Chào hỏi
            2. Hiển thị ngày, giờ
            3. Mở trang web, ứng dụng
            4. Tìm kiếm trên Google
            5. Tìm nhạc trên Youtube
            6. Gửi email
            7. Dự báo thời tiết 
            8. Thay đổi hình nền máy tính
            9. Đọc báo hôm nay
            10. Kể bạn biết về thế giới """)

        elif "tên" in text: 
            speak("Tôi là CHATBOT! Tôi có thể giúp gì cho bạn?")

        elif "tuổi" in text: 
            speak("Tôi chỉ là robot nên không có tuổi!")

        elif "ở đâu" in text: 
            speak("Tôi đang ở cùng với bạn!")

        elif "làm gì" in text:
            speak("Tôi là một nô lệ của bạn!")

        elif "khỏe không" in text:
            speak("Tôi khỏe, cảm ơn, còn bạn!")

        elif "nghe" in text:
            speak("Tôi vẫn đang lắng nghe!")

        elif "tốt" in text or "giỏi" in text or "cảm ơn" in text:
            speak("Ok baby!")

        elif "cười" in text:
            speak(GoogleTranslator(source="auto", target="vi").translate(pyjokes.get_joke(language="en", category="all")))

        # Hỏi gì khó vậy
        else:
            speak("Tôi không biết!")