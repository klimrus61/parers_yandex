import requests


class CookieStillAliveException(Exception):
    'Куки все еще живые'
    pass


def get_fresh_cookie(old_cookie: dict) -> dict:
    if old_cookie: 
        cookies = old_cookie
    else:
        raise Exception('Куки не были получены!')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://partner.yandex.ru/',
        'Connection': 'keep-alive',
        # 'Cookie': 'yandexuid=3250355031675439683; _yasc=eUQCefdSvq1IC089mE1tQ9j7s6oPoLOmX6SsW9S5S0/6LMulYFeJDCWh+qqFVws=; yp=1990800116.multib.1#1990804913.udn.cDp0ZXN0dGVzdHQzc3Rvdml5#1676896921.szm.2:1600x1000:1600x875; i=2inYfwBWWI6gdhXFtJ09eszae+pjTKLg5mdIYP0yFZA3tDSbbbkaPvkJVroKG25Y1ipN9K0EmndFOiNx/Id1bD+2FMw=; yuidss=3250355031675439683; ymex=1990799685.yrts.1675439685#1990799685.yrtsi.1675439685; gdpr=0; _ym_uid=1675439687596707038; _ym_d=1675439687; yashr=812306331675439686; uniqueuid=670491031675439686; L=XwZVQFNtdFJiZXFCQXl1bXANdHAOD01YR1I9NhFdHkAXZCdCFTgwLg==.1675444913.15242.397676.dada423e268ec6e3e41eb2e05b07ade6; yandex_login=testtestt3stoviy; lah=2:1739382437.10020595.Tz3oIJlvQzr3kT1W.IcOpdawHxIMYdVjdWzkx1Bb0TG3v12IaEAUEXKnJMD0HceaZwBuoGDCU4tb_CQsF.YXLtQ-_QOmKTbwD_CcVLBQ; mda2_beacon=1676310319078; mda2_domains=ya.ru; is_gdpr=0; is_gdpr_b=CPvaURDKpAE=; ilahu=1675473700; Session_id=3:1675444913.5.0.1675444913544:aX2NXg:44.1.2:1|1751329321.0.2|3:10265053.423479.3Qz51OADoWVtOnKn74-732o1aCQ; sessionid2=3:1675444913.5.0.1675444913544:aX2NXg:44.1.2:1|1751329321.0.2|3:10265053.423479.fakesign0000000000000000000; sessguard=1.1676310319.1675444913544:aX2NXg:44..3.500:32473.GKh7unwz.UZEPXA7N2nEnKAz19vfayltrnGI; _ym_isad=2; _ym_visorc=b; Cookie_check=CheckCookieCheckCookie; ys=udn.cDp0ZXN0dGVzdHQzc3Rvdml5#c_chck.3787545873',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
    }

    params = {
        'retpath': 'https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fpartner2.yandex.ru%2F',
    }

    response = requests.get('https://passport.yandex.ru/auth/update', params=params, cookies=cookies, headers=headers, allow_redirects=False)

    set_cookies = response.headers['Set-Cookie']
    session_id = None
    session_id2 = None
    for cookie in set_cookies.split(';'):
        cookie = cookie.strip()
        if 'Session_id' in cookie:
            session_id = cookie.split('=')[-1]
        if 'sessionid2' in cookie:
            session_id2 = cookie.split('=')[-1]
        if session_id and session_id2:
            break
    if not session_id or not session_id2:
        raise CookieStillAliveException('Скорее всего куки еще живые!')
    new_cookies = {
        'Session_id': f'{session_id}',
        'sessionid2': f'{session_id2}',
    }
    return new_cookies

if __name__ == "__main__":
    test_old_cookie = {
        'Session_id': '3:1675444913.5.0.1675444913544:aX2NXg:44.1.2:1|1751329321.0.2|3:10265053.423479.3Qz51OADoWVtOnKn74-732o1aCQ',
        'sessionid2': '3:1675444913.5.0.1675444913544:aX2NXg:44.1.2:1|1751329321.0.2|3:10265053.423479.fakesign0000000000000000000',
    }
    print(get_fresh_cookie(test_old_cookie))
