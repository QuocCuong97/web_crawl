import telegram
import objects
from websites import NewsCloud365, TecAdmin, Techrum
from json_execute import load_from_json, export_to_json
from database import Mariadb
from bot import Telegram_Bot



val = load_from_json('/home/cuongnq/code/settings.json')
host = val[0]["db_host"]
user = val[0]['db_username']
passwd = val[0]['db_password']
db = val[0]['db_database']
token = val[1]['telegram_token']
chatid = val[1]['telegram_chatid']

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

        bot = Telegram_Bot(token, chatid)
        result = mydb.query(myconnect, table)
        if result == '0':
            link = mydb.newest_link(myconnect, table)
            bot.send_message(link)
            mydb.update_true(myconnect, table)
        else:
            pass
        mydb.close(myconnect)

def main():
    web_need_crawl_1 = NewsCloud365()
    web_need_crawl_2 = TecAdmin()
    web_need_crawl_3 = Techrum()
    crawl(web_need_crawl_1, web_need_crawl_2, web_need_crawl_3)

main()








