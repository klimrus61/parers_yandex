from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from models import Game, Base
from roblox_parser import get_data_from_roblox


class Database:

    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///roblox.db")
        if not inspect(self.engine).has_table(Game.__tablename__):
            Base.metadata.create_all(self.engine)
            print('Создана база данных')
        self.session = Session(self.engine)


    def write_parse_data(self, data_to_game_table):
        '''Записывает спарсенные данные функцией get_data_from_roblox 
        в таблицу game базы данных roblox'''
        try:
            to_database = [Game(group=game['group'], \
                                title=game['title'], \
                                active_players=game['active_players'], \
                                total_up_votes=game['total_up_votes'], \
                                total_down_votes=game['total_down_votes'], \
                                description=game['description'],) \
                                for game in data_to_game_table]
            self.session.add_all(to_database)
            self.session.commit()
            print('Данные успешно добавлены!')
        except Exception as err:
            self.session.rollback()
            self.session.commit()
            print(err)



if __name__ == "__main__":
    data_to_game_table = get_data_from_roblox()
    if data_to_game_table:
        Database().write_parse_data(data_to_game_table)
    else:
        print('Список для записи в базу пустой')