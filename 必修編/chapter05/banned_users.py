banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'

if user not in banned_users:
    print(f"{user.title()}はコメントを書き込めます。")
else:
    print("あなたはバンされています。")

