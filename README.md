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
- Phần thông tin về Telegram Bot :
    ```sh
    "telegram_token": "<Token của Bot đã tạo trước đó",
    "telegram_chatid": "<Chat-id của Bot>"
    ```
**B4 :** Chạy chương trình :
```
python3 main.py
```
**B5 :** Lên lịch trình crontab ( thời gian khuyến nghị : mỗi `10p` )
```
echo "*/6 * * * * root path_to_file_main.py" >> /etc/crontab
