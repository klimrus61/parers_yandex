import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36',
}

data={"entity_fields":["block_level"],"dimension_fields":["date|day"],"fields":["partner_wo_nds"],"lang":"ru","levels":[{"id":"payment"}],"limits":{"limit":500,"offset":0},"period":["2023-01-05","2023-02-03"],"pretty":1,"stat_type":"main","currency":"RUB","top_keys":16,"top_keys_order_by":[{"field":"partner_wo_nds","dir":"desc"}],"order_by":[{"field":"date","dir":"desc"},{"field":"partner_wo_nds","dir":"desc"},{"field":"block_level","dir":"asc"}]}

cookie_str="i=JkVETSgy7Tob7+3Texodr5Y9/bXqcxvikSB+QgH0rBdjy+DU0qkTD08bWnmQnluBU70r6UrJycM43b4RrjYFm8H6Auk=; yandexuid=4450842971675421605; yuidss=4450842971675421605; yashr=5942129531675421606; gdpr=0; _ym_uid=1666712689583843156; _ym_d=1675421609; _ym_isad=1; ymex=1990781605.yrts.1675421605#1990781605.yrtsi.1675421605; is_gdpr=0; is_gdpr_b=CPvaURDFpAEoAg==; Session_id=3:1675423200.5.0.1675423200949:armivA:5c.1.2:1|1751329321.0.2|3:10265041.892530.yYheX4A4gVT-T0fJ2IrHNm7o3Wk; sessionid2=3:1675423200.5.0.1675423200949:armivA:5c.1.2:1|1751329321.0.2|3:10265041.892530.fakesign0000000000000000000; L=XwZVQFNtdFJiZXFCQXl8Z3IBe3EIAE9fR1I9NhFdHkAXZCdCFTgwLg==.1675423200.15242.333513.dfd8ca4915a19439d04c7faf36a4a601; yandex_login=testtestt3stoviy; ys=udn.cDp0ZXN0dGVzdHQzc3Rvdml5#c_chck.3635091954; _yasc=0RVoFjv+ZL9t4kyzfDEEbVn+soUbL8w3TACXe7LmqNoV13gGIARMHSHHwo+uQM9w4oS1FGA=; _ym_visorc=w; yp=1675507253.uc.ru#1675507253.duc.ru#1706957607.brd.6300000000#1706957607.cld.2270482#1677413051.csc.1#1675434053.gpauto.47_293064:39_661057:140:1:1675426853#1675947083.mcv.0#1990782940.pcs.0#1702315681.pgp.5_27846327#1705141875.stltp.serp_bk-map_1_1673605875#1675947083.szm.2:1600x1000:1552x861#1677964068.ygu.1#1990780984.multib.1#1990783200.udn.cDp0ZXN0dGVzdHQzc3Rvdml5"
def make_cookiejar_dict(cookies_str):
    # alt: `return dict(cookie.strip().split("=", maxsplit=1) for cookie in cookies_str.split(";"))`
    cookiejar_dict = {}
    for cookie_string in cookies_str.split(";"):
        # maxsplit=1 because cookie value may have "="
        cookie_key, cookie_value = cookie_string.strip().split("=", maxsplit=1)
        cookiejar_dict[cookie_key] = cookie_value
    return cookiejar_dict

cj = requests.cookies.cookiejar_from_dict(make_cookiejar_dict(cookies_str=cookie_str))

s = requests.Session()
s.headers.update(headers)
s.cookies = cj
s.get('https://partner.yandex.ru/v2/dashboard')
r = s.post('https://partner.yandex.ru/restapi/v1/api/statistics/get_statistics?stat_type=main', data=data)
print(r.status_code,'\n', r.headers, '\n\n', r.request.headers, r.text)
