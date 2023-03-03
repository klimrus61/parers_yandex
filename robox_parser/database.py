from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from models import Game, Base
from roblox_parser import get_data_from_roblox

class Database:

    def __init__(self) -> None:
        # db.connect()
        self.engine = create_engine("sqlite:///roblox.db")
        if not inspect(self.engine).has_table('roblox.db'):
            Base.metadata.create_all(self.engine)
            print('Создана база данных')

    def write_parse_data(self, data_to_game_table):
        '''Записывает спарсенные данные функцией get_data_from_roblox 
        в таблицу game базы данных roblox'''
        if data_to_game_table:
            with Session(self.engine) as session:
                session.add_all([Game(**game) for game in data_to_game_table])
                session.commit()
                print('Данные успешно добавлены!')
        else:
            print('Передан пустой список')


if __name__ == "__main__":
    data_to_game_table = get_data_from_roblox()
    Database().write_parse_data(data_to_game_table)
