from mongoengine import Document,StringField,ListField

class Prev_news(Document):
    category = ListField()
    title = StringField()
    description = StringField()
    pubdate = StringField()
    source_id = StringField()
    country = ListField()
    link = StringField()