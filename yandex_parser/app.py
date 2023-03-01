import parser_statistics
import fresh_cookies

test_old_cookie = {
    'Session_id': '3:1675444913.5.0.1675444913544:aX2NXg:44.1.2:1|1751329321.0.2|3:10265053.423479.3Qz51OADoWVtOnKn74-732o1aCQ',
    'sessionid2': '3:1675444913.5.0.1675444913544:aX2NXg:44.1.2:1|1751329321.0.2|3:10265053.423479.fakesign0000000000000000000',
}
test_old_cookie2 = {
    'Session_id': '3:1676313403.5.0.1675444913544:aX2NXg:44.1.2:1|1751329321.0.2|3:10265535.899263.YvnA4Jiz0X-oIc8VcHic60jTSWI',
    'sessionid2': '3:1676313403.5.0.1675444913544:aX2NXg:44.1.2:1|1751329321.0.2|3:10265535.899263.fakesign0000000000000000000',
}


new_cookie = fresh_cookies.get_fresh_cookie(test_old_cookie)

print(parser_statistics.parser(new_cookie))
