from peewee import SqliteDatabase, Model, CharField, TextField, IntegerField
from roblox_parser import get_data_from_roblox

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

db.connect()
db.create_tables([Game])

data_to_game_table = get_data_from_roblox()

if data_to_game_table:
    query = Game.insert_many(data_to_game_table)
    query.execute(db)
    print("Данные успешно добавлены")
else:
    raise Exception('Список пуст')

print('Закрытие соединения')
db.close()
