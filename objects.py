class ObjectCrawl:

    def __init__(self, title, link, time_created, author, source):
        self.title = title
        self.link = link
        self.time_created = time_created
        self.author = author
        self.source = source

    def show_object(self):
        message = 'Title - {}, Link - {}, Time Created - {}, Author - {}, Source - {}'.format(
            self.title,
            self.link,
            self.time_created,
            self.author,
            self.source
        )
        print(message)

    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "time_created": self.time_created,
            "author": self.author,
            "source": self.source
        }
