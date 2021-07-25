l_pork=['豬肉']
l_lobo=['胡蘿蔔']
l_bech=['荸薺']
while True:
  print('\n選擇步驟')
  print("\n1  增加菜單")
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
      l_lobo.append(l)
      ll=input('\n刀工:')
      l_lobo.append(ll)
    if t=='b':
      b=input('\n輸入克數:')
      l_lobo.append(b+'g')
      bb=input('刀工:')
      l_lobo.append(bb)
    if t=='c':
      p=input('\n輸入克數:')
      l_lobo.append(p+'g')
      pp=input('刀工:')
      l_lobo.append(pp)

  if q=='2':
    print(l_lobo)
    print(l_bech)
    print(l_pork)