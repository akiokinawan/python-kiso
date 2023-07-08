first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"こんにちは{full_name.title()}！"
print(message)

first_name = "Ada"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
# 先頭だけ大文字ならTrue それ以外はFalse
message = f"こんにちは{full_name.istitle()}！"
print(message)
