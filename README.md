# Guides
**B1 :** Clone repo **web_crawl** :
```
git clone https://github.com/QuocCuong97/web_crawl
```
**B2 :** Tải về và cài đặt các gói cần thiết ( yêu cầu đã cài đặt **Python3**, **PIP** ) :
```
cd web_crawl
sudo pip3 install -r requirements.txt
```
**B3 :** Điền các thông tin cần thiết vào file `settings.json` :
- Phần thông tin về database :
    ```sh
    "db_host": "<Host MariaDB/MySQL>",
    "db_username": "<User có quyền truy cập database>",
    "db_password": "<Mật khẩu user>",
    "db_database": "web_crawling"    # Tạo trước 1 database để chứa dữ liệu crawl
    ```
    > Chú ý khi tạo database :
    ```sh
    CREATE DATABASE web_crawl CHARACTER SET utf8 COLLATE utf8_general_ci;
    ```
- Phần thông tin về Telegram Bot :
    ```sh
    "telegram_token": "<Token của Bot đã tạo trước đó",
    "telegram_chatid": "<Chat-id của Bot>"
    ```
- Phần thông tin về Email Bot :
    ```sh
    "email_sender": "<Email của sender",
    "password_sender": "<Password của sender",
    "mail_target": "<Đường dẫn file chứa thông tin các email cần gửi>"
    ```
    - File `mail_target.txt` : chứa thông tin các email cần gửi
        ```sh
        abc@gmail.com
        bcd@gmail.com
        cde@outlook.com

        # Phải đưa trỏ chuột xuống dòng dưới cùng
        ```
**B4 :** Chạy chương trình :
```
python3 main.py
```
**B5 :** Lên lịch trình crontab ( thời gian khuyến nghị : mỗi `10p` )
```
echo "*/5 * * * * root path_to_file_main.py" >> /etc/crontab
```

>## **Các trang web được crawl trong chương trình**
- https://news.cloud365.vn/
- https://tecadmin.net/
- https://www.techrum.vn
- https://www.digitalocean.com/community/tutorials
- https://cuongquach.com/category/linux/