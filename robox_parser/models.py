from peewee import SqliteDatabase, Model, CharField, TextField, IntegerField


db = SqliteDatabase('roblox.db')

class Game(Model):
    '''Модель спарсиной игры'''
    grup = CharField()
    title = CharField()
    active_players = IntegerField()
    total_up_votes = IntegerField()
    total_down_votes = IntegerField()
    description = TextField()

    class Meta:
        database = db

