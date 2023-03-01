# Приложение для записи данных в базу
from models import db, Game
from roblox_parser import get_data_from_roblox


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
