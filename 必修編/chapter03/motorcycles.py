motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

for moto in motorcycles:
  if moto[0] == 'y':
    print(moto)
  else:
    print("no match")  
    

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()}は私には高すぎます。")
