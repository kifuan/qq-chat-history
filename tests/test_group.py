from qq_chat_history import Parser


lines = '''
===
假装我是 QQ 自动生成的文件头
===

1883-03-07 11:22:33 A<someone@example.com>
关注永雏塔菲喵
关注永雏塔菲谢谢喵

1883-03-07 12:34:56 B(123123)
TCG

1883-03-07 13:24:36 C(456456)
TCG

1883-03-07 22:00:51 A<someone@example.com>
塔菲怎么你了
'''.strip().splitlines()

expected_lines = [
    {'date': '1883-03-07 11:22:33', 'id': 'someone@example.com', 'name': 'A', 'content': '关注永雏塔菲喵\n关注永雏塔菲谢谢喵'},
    {'date': '1883-03-07 12:34:56', 'id': '123123', 'name': 'B', 'content': 'TCG'},
    {'date': '1883-03-07 13:24:36', 'id': '456456', 'name': 'C', 'content': 'TCG'},
    {'date': '1883-03-07 22:00:51', 'id': 'someone@example.com', 'name': 'A', 'content': '塔菲怎么你了'}
]


def test_group():
    parser = Parser.get_instance('group')
    parsed_lines = list(parser.parse(lines))
    assert parsed_lines == expected_lines
