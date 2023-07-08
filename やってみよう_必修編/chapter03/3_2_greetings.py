names = {
  'first' : ['やすだ', 'てらだ', 'しみずかわ'],
  'last' : ['とも', 'てら', 'しみず']
}
print(len(names.values()))
for i in range(len(names.values())+1):
  print(names['first'][i]+names['last'][i])
# full_name = []
# for k,values in names.items():
#   for v in values:
#     full_name.append(v)

# print(f"こんにちは、{full_name}さん！")
