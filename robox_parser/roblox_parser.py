import requests
import random


class RobloxParser:
    '''Парсит https://www.roblox.com/discover по категориям'''
    def __init__(self) -> None:
        self.session = requests.Session()
        

    def update_user_agent(self, path_to_user_agents='robox_parser\\user_agents.txt') -> None:
        'получает и устанавливает рандомного user_agent из файла по path_to_user_agents'
        with open(path_to_user_agents) as f:
            user_agents = f.readlines()
            index = int(random.random() * len(user_agents))
            user_agent = user_agents[index].strip()
        self.session.headers.update({'user-agent': user_agent})

    def _get_game_sorts_data(self) -> dict:
        ''''''
        params = {'gameSortsContext': 'GamesDefaultSorts'}
        response = self.session.get('https://games.roblox.com/v1/games/sorts', params=params)
        data = response.json()
        return data

    def _get_game_list_of_group(self, params) -> dict:
        ''''''
        response = self.session.get(
                'https://games.roblox.com/v1/games/list',
                params=params,
        )
        game_list = response.json()['games']
        return game_list

    def get_data_to_db(self) -> list[dict]:
        '''Возвращает список словарей имеющий структуру:
        [
            {"group": str,
            "title": str,
            "active_players: int,
            "total_up_votes": int,
            "total_down_votes": int,
            "description": str,},
        ]
        '''
        to_database = []
        sorts_data = self._get_game_sorts_data()
        games_sorts = sorts_data['sorts']

        for sort in games_sorts:
            params = {
                'sortToken': sort['token'],
                'gameSetTargetId': sort['gameSetTargetId'],
                'pageContext.pageId': sorts_data['pageContext']['pageId'],
            }
            game_list = self._get_game_list_of_group(params)
            for game in game_list:
                game_data = {
                    'group': sort['displayName'],
                    'title': game['name'],
                    'active_players': game['playerCount'],
                    'total_up_votes': game['totalUpVotes'],
                    'total_down_votes': game['totalDownVotes'],
                    'description': game['gameDescription'],
                }
                to_database.append(game_data)
        return to_database

if __name__ == "__main__":
    # print(get_data_from_roblox())
    # print(get_user_agent('robox_parser\\user_agents.txt'))
    roblox_parser = RobloxParser()
    roblox_parser.update_user_agent('robox_parser\\user_agents.txt')
    print(roblox_parser.get_data_to_db())