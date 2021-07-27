l1=['豬肉','?','?']
l2=['胡蘿蔔','?','?']
l3=['荸薺','?','?']
while True:
  print('\n選擇步驟')
  print("\n1  修改菜單")
  print("\n2  顯示菜單")
  q=input('\n輸入步驟:')
  if q=='1':
    print('\n選擇材料')
    print('\na  胡蘿蔔')
    print('\nb  荸薺')
    print('\nc  豬肉')
    t=input('\n輸入代號:')
    if t=='a':
      l=input('\n輸入克數:')
      l2.pop(1)
      l2.append(l)
      ll=input('\n刀工:')
      l2.pop(2)
      l2.append(ll)
    if t=='b':
      b=input('\n輸入克數:')
      l3.append(b+'g')
      bb=input('刀工:')
      l3.append(bb)
    if t=='c':
      p=input('\n輸入克數:')
      l1.append(p+'g')
      pp=input('刀工:')
      l1.append(pp)

  if q=='2':
    print(l1)
    print(l2)
    print(l3)