def greet_users(names):
    """リストの各ユーザーに対してシンプルなあいさつを出力する"""
    for name in names:
        msg = f"こんにちは{name.title()}！"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
print(type(usernames))
greet_users(usernames)
