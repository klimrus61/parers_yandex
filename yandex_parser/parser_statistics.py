import requests


def parser(cookies: dict):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'application/vnd.api+json',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://partner.yandex.ru/v2/statistics/constructor/?page%5Bsize%5D=100&page%5Bnumber%5D=1&period%5BendDate%5D=1675382400000&period%5BstartDate%5D=1672876800000&statType=main&currency=RUB&dimensionFields=date%7Cday&entityFields=block_level&fields=partner_wo_nds&filter=%5B%22AND%22%2C%5B%5B%22adfox_block%22%2C%22%3D%22%2Ctrue%5D%5D%5D&openSelfEmployedForm=false&openPayoneerForm=false&openOfferYandexGamesNonResident=false&openOfferYandexGamesResident=false&openOfferYandexGamesBy=false',
        'Content-Type': 'application/vnd.api+json',
        'x-skeleton-disabled': 'true',
        # 'x-request-id': '42508cfa-df88-4232-8dc1-2a68462f5b70',
        # 'x-session-id': '665a295402f09876c52a81434eacf001',
        # 'X-Frontend-Authorization': 'token 95fa8644fc633f6812b841428159cccf',
        'Origin': 'https://partner.yandex.ru',
        'Connection': 'keep-alive',
        # 'Cookie': 'yandexuid=3250355031675439683; _yasc=VTIaZVpXWBLp3DGgGvZfibWoRvqgkV0MAOQosbwf6/qA6q53SPRf3rcOib0wx7s=; yp=1676044486.szm.2:1600x1000:1600x875#1990800116.multib.1#1990800132.udn.cDp0ZXN0dGVzdHQzc3Rvdml5; i=2inYfwBWWI6gdhXFtJ09eszae+pjTKLg5mdIYP0yFZA3tDSbbbkaPvkJVroKG25Y1ipN9K0EmndFOiNx/Id1bD+2FMw=; yuidss=3250355031675439683; ymex=1990799685.yrts.1675439685#1990799685.yrtsi.1675439685; gdpr=0; _ym_uid=1675439687596707038; _ym_d=1675439687; yashr=812306331675439686; _ym_isad=2; _ym_visorc=b; ys=udn.cDp0ZXN0dGVzdHQzc3Rvdml5#c_chck.2284807965; L=XwZVQFNtdFJiZXFCQXl3ZHMOfH4BAUlTR1I9NhFdHkAXZCdCFTgwLg==.1675440132.15242.360543.abadba0394e098907c541e9e8e31aa46; yandex_login=testtestt3stoviy; is_gdpr=0; is_gdpr_b=CPvaURDKpAE=; Session_id=3:1675440132.5.0.1675440132021:aX2NXg:14.1.2:1|1751329321.0.2|3:10265049.383440.KwNhTM97RGPd6AfFcG48hIYi-tw; sessionid2=3:1675440132.5.0.1675440132021:aX2NXg:14.1.2:1|1751329321.0.2|3:10265049.383440.fakesign0000000000000000000',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'stat_type': 'main',
    }

    data = '{"data":{"entity_fields":["block_level"],"dimension_fields":["date|day"],"fields":["partner_wo_nds"],"lang":"ru","levels":[{"filter":["AND",[["adfox_block","=",true]]],"id":"payment"}],"limits":{"limit":500,"offset":0},"period":["2023-01-05","2023-02-03"],"pretty":1,"stat_type":"main","currency":"RUB","top_keys":16,"top_keys_order_by":[{"field":"partner_wo_nds","dir":"desc"}],"order_by":[{"field":"date","dir":"desc"},{"field":"partner_wo_nds","dir":"desc"},{"field":"block_level","dir":"asc"}]}}'

    response = requests.post(
        'https://partner.yandex.ru/restapi/v1/api/statistics/get_statistics',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    auth = response.headers['X-Frontend-Authorization']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'application/vnd.api+json',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://partner.yandex.ru/v2/dashboard',
        'Content-Type': 'application/vnd.api+json',
        'x-skeleton-disabled': 'true',
        # 'x-request-id': 'c24eeca8-6155-4368-97b7-312fdb9b7894',
        # 'x-session-id': '47b570d43c464faa6f95122f63462152',
        'X-Frontend-Authorization': f'{auth}',
        'Origin': 'https://partner.yandex.ru',
        'Connection': 'keep-alive',
        # 'Cookie': 'yandexuid=3250355031675439683; _yasc=Zwgwox/7XkblKUCba484WT/U7YFAdEh79CfI7VoSFJsJlDtcgpr6U8ZnQqiStqs=; yp=1676044486.szm.2:1600x1000:1600x875#1990799697.udn.cDp0ZXN0dGVzdHQzc3Rvdml5; i=2inYfwBWWI6gdhXFtJ09eszae+pjTKLg5mdIYP0yFZA3tDSbbbkaPvkJVroKG25Y1ipN9K0EmndFOiNx/Id1bD+2FMw=; yuidss=3250355031675439683; ymex=1990799685.yrts.1675439685#1990799685.yrtsi.1675439685; gdpr=0; _ym_uid=1675439687596707038; _ym_d=1675439687; yashr=812306331675439686; _ym_isad=2; _ym_visorc=b; Session_id=3:1675439697.5.0.1675439697599:aX2NXg:12.1.2:1|1751329321.0.2|3:10265049.638744.FyzdAaN1uNe-lUrTAyTMTPHoi00; sessionid2=3:1675439697.5.0.1675439697599:aX2NXg:12.1.2:1|1751329321.0.2|3:10265049.638744.fakesign0000000000000000000; ys=udn.cDp0ZXN0dGVzdHQzc3Rvdml5#c_chck.3967300900; L=XwZVQFNtdFJiZXFCQXl9ZHENencJAU1YR1I9NhFdHkAXZCdCFTgwLg==.1675439697.15242.385261.2e0965846684156b8f057e6c07f8c6ee; yandex_login=testtestt3stoviy; is_gdpr=0; is_gdpr_b=CPvaURDKpAE=',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'stat_type': 'main',
    }

    data = '{"data":{"entity_fields":["block_level"],"dimension_fields":["date|day"],"fields":["partner_wo_nds"],"lang":"ru","levels":[{"id":"payment"}],"limits":{"limit":500,"offset":0},"period":["2023-01-05","2023-02-03"],"pretty":1,"currency":"RUB","top_keys":16,"top_keys_order_by":[{"field":"partner_wo_nds","dir":"desc"}],"order_by":[{"field":"date","dir":"desc"},{"field":"partner_wo_nds","dir":"desc"},{"field":"block_level","dir":"asc"}]}}'

    response = requests.post(
        'https://partner.yandex.ru/restapi/v1/api/statistics/get_statistics',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return response.json()

