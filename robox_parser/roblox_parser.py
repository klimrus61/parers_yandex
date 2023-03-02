import requests
from fake_useragent import UserAgent


def get_data_from_roblox() -> list[dict]:
    '''Возвращает список словарей имеющий структуру:
    [
        {"grup": str,
        "title": str,
        "active_players: int,
        "total_up_votes": int,
        "total_down_votes": int,
        "description": str,},
    ]
    '''
    parsed_games = []
    user_agent = UserAgent()
    session = requests.Session()
    session.headers.update({'user-agent': user_agent.random})
    response = session.get('https://games.roblox.com/v1/games/sorts', params={})

    data = response.json()
    game_sorts = data['sorts']
    for sort in game_sorts:
        params = {
            'sortToken': sort['token'],
            'gameSetTargetId': sort['gameSetTargetId'],
            'pageContext.pageId': data['pageContext']['pageId'],
        }

        second_response = session.get(
            'https://games.roblox.com/v1/games/list',
            params=params,
        )
        games = second_response.json()['games']
        for game in games:
            game_data = {
                'grup': sort['displayName'],
                'title': game['name'],
                'active_players': game['playerCount'],
                'total_up_votes': game['totalUpVotes'],
                'total_down_votes': game['totalDownVotes'],
                'description': game['gameDescription'],
            }
            parsed_games.append(game_data)
    return parsed_games


if __name__ == "__main__":
    print(get_data_from_roblox())
