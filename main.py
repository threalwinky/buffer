#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import random
import string
import base64
import time
from unidecode import unidecode
options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox()

def encode64(text):
    b = text.encode("ascii")
    b2 = base64.b64encode(b)
    return b2.decode("ascii")

def getName():
    lastName = [
        "Nguyễn",
        "Trần",
        "Lê",
        "Phạm",
        "Hoàng",
        "Vũ",
        "Phan",
        "Bùi",
        "Võ",
        "Huỳnh",
        "Đỗ",
        "Ngô",
        "Hồ",
        "Đăng",
        "Hà",
        "Dương",
        "Mai",
        "Lâm",
        "Bảo",
    ]
    firstName = [
        "Anh",
        "Linh",
        "Thanh",
        "Tuấn",
        "An",
        "Hùng",
        "Trang",
        "Phương",
        "Dung",
        "Nam",
        "Thảo",
        "Huy",
        "Ngọc",
        "Sơn",
        "Hạnh",
        "Nguyên",
        "Vân",
        "Nga",
        "Long",
        "Minh",
        "Tiến",
        "Đạt",
        "Đại",
        "Nhi",
        "An",
        "Vy",
        "Long",
        "Khang",
        "Vũ",
        "Minh",
        "My",
        "Hằng",
        "Thảo",
        "Phú",
        "Nguyên",
        "Nguyễn",
        "Như"
    ]
    return random.choice(lastName) + " " + random.choice([random.choice(firstName) + ' ', '']) + random.choice(firstName)

def getSchool():
    school = [
        "Chuyên Lê Hồng Phong",
        "Chuyên Trần Đại Nghĩa",
        "Trần Phú",
        "Trần Phú",
        "Nguyễn Thượng Hiền",
        "Trưng Vương",
        "Bùi Thị Xuân",
        "Lê Quý Đôn",
        "Nguyễn Thị Minh Khai",
        "Marie Curie",
        "Trần Khai Nguyên",
        "Trần Hưng Đạo",
        "Nguyễn Công Trứ",
        "Võ Trường Toản",
        "Nguyễn Khuyến",
        "Mạc Đĩnh Chi",
        "Tây Thạnh",
        "Võ Thị Sáu",
        "Hoàng Hoa Thám",
        "Phú Nhuận",
        "Nguyễn Hữu Huân",
        "Thủ Đức",
        "Nguyễn Hữu Cầu",
        "Phan Châu Trinh",
        "Bình Phú",
        "Quốc Trí",
        "Phú Lâm",
        "Lê Thánh Tôn",
        "Ngô Quyền",
        "Đại học Bách Khoa TPHCM",
        "Đại học KHTN TPHCM",
        "ĐH HCMUT",
        "ĐH HCMUS",
        "ĐH UIT",
        "Đại học Công nghệ thông tin TPHCM",
        "Đại học Hoa Sen TPHCM",
        "Đại học FPT TPHCM",
        "Đại học TPHCM",
    ]
    return random.choice(school)
pwd = ""
def getPhoneNumber():
    num = "0" + random.choice(["3", "7", "5", "8", "9"])

    for i in range(8):
        num += str(random.randint(0, 9))
    return num

def getClass(name):
    if (name[0] == 'Đ'):
        return random.choice(["KHMT", "CNTT", "KTMT"])
    return random.choice(["10C", "11B", "12A", "10A", "12C"]) + str(random.randint(1, 16))

def login(phone):
    driver.get("https://khoinghieptre.edu.vn/dang-nhap")
    email = driver.find_element("xpath", '//*[@id="name"]')
    email.send_keys(em)
    password = driver.find_element("xpath", '//*[@id="password"]')
    password.send_keys(p)
    print(p)
    # Submit
    driver.find_element("xpath", "/html/body/div[2]/form/div/div[3]/button").click()

def register():
    driver.get("https://khoinghieptre.edu.vn/dang-ky-tham-gia")
    t = getName()
    driver.find_element("xpath", '//*[@id="name"]').send_keys(t)
    phone = getPhoneNumber()
    driver.find_element("xpath", '//*[@id="phone"]').send_keys(phone)
    global em
    em = unidecode(t.lower().replace(' ', '') + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + "0" + str(random.randint(6, 8)) + "@gmail.com")
    driver.find_element("xpath", '//*[@id="email"]').send_keys(em)
    global p
    p = ""
    for i in range(random.randint(7, 15)):
        p += random.choice([random.choice(string.ascii_letters), str(random.randint(0, 9))])
    driver.find_element("xpath", '//*[@id="password"]').send_keys(p)
    driver.find_element("xpath", '/html/body/div[2]/form/div/div[5]/button').click()
    return phone

def vote():
    driver.get("https://khoinghieptre.edu.vn/chi-tiet-bai/gian-phoi-tu-dong-hoa")
    driver.find_element("xpath", '/html/body/div[2]/div/div[2]/div[2]/div[2]/button').click()
    t = getSchool()
    driver.find_element("xpath", '//*[@id="truongUser"]').send_keys("THPT " + t)
    driver.find_element("xpath", '//*[@id="lopUser"]').send_keys(getClass(t))
    driver.find_element("xpath", '/html/body/div[3]/div/div/form/div[2]/button[1]').click()

def logout():
    driver.get("https://khoinghieptre.edu.vn")
    driver.find_element("xpath", '/html/body/header/div[1]/div/div/div[2]/div/a').click()

while True:
    pwd = ""
    phone = register()
    print("New account created.")
    print("Phone: " + phone)
    print("Password: " + p)
    print("Mail: " + em)

    login(phone)
    vote()
    
    logout()

    time.sleep(random.randint(1, 2))
