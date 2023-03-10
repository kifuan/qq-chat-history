from qq_chat_history import parse, Message


lines = '''
=========
假装我是 QQ 自动生成的文件头
=========


1883-03-07 11:22:33 A
关注永雏塔菲喵
关注永雏塔菲谢谢喵

1883-03-07 12:34:56 B
TCG

1883-03-07 22:00:51 A
塔菲怎么你了
'''.strip().splitlines()

expected_messages = [
    Message(date='1883-03-07 11:22:33', id='A', name='A', content='关注永雏塔菲喵\n关注永雏塔菲谢谢喵'),
    Message(date='1883-03-07 12:34:56', id='B', name='B', content='TCG'),
    Message(date='1883-03-07 22:00:51', id='A', name='A', content='塔菲怎么你了'),
]


def test_private() -> None:
    messages = list(parse(lines))
    assert messages == expected_messages
