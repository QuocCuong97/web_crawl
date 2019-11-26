from websites import NewsCloud365, TecAdmin, Techrum, DigitalOcean, CuongQuach
from json_execute import load_from_json, export_to_json
from database import Mariadb
from bot import Telegram_Bot, Email_Bot
import objects


val = load_from_json('/home/cuongnq/code/settings.json')
# database
host = val[0]["db_host"]
user = val[0]['db_username']
passwd = val[0]['db_password']
db = val[0]['db_database']
# telegram
token = val[1]['telegram_token']
chatid = val[1]['telegram_chatid']
# email
sender = val[2]['email_sender']
sender_passwd = val[2]['password_sender']
target_file = val[2]['mail_target']

def crawl(*args):
    for x in args: 
        table = x.source.lower()
        lst = x.get_objects()

        export_to_json(lst, '/home/cuongnq/code/output.json')
        lst.reverse()

        mydb = Mariadb(host, user, passwd, db)
        myconnect = mydb.connect()
        mydb.create_table(myconnect, table)
        mydb.insert(lst, myconnect, table)
        mydb.query(myconnect, table)

        bot_1 = Telegram_Bot(token, chatid)
        # bot_2 = Email_Bot(sender, sender_passwd)
        result = mydb.query(myconnect, table)
        if result == '0':
            link = mydb.newest_link(myconnect, table)
            bot_1.send_message(link)
            # bot_2.get_target(target_file)
            # bot_2.send_email('New Post from {}'.format(x.source), link)
            mydb.update_true(myconnect, table)
        else:
            pass

def main():
    web_1 = NewsCloud365()
    web_2 = TecAdmin()
    web_3 = Techrum()
    web_4 = DigitalOcean()
    web_5 = CuongQuach()
    crawl(web_1, web_2, web_3, web_4, web_5)

main()