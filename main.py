l1 = ['豬肉', '?', '?']
l2 = ['胡蘿蔔', '?', '?']
l3 = ['荸薺', '?', '?']
l4 = ['薑', '?', '?']
l5 = ['蔥', '?', '?']
l6 = ['胡椒粉', '?']
l7 = ['味精', '?']
l8 = ['太白粉', '?']
l9 = ['鹽', '?']
l10 = ['香油', '?']
l11 = ['醬油', '?']
l12 = ['酒', '?']
l13 = ['太白粉', '?']
l14 = ['麵粉', '?']
while True:
    print('\n選擇動作')
    print("1  修改菜單")
    print("2  顯示菜單")
    print('3  顯示流程')
    q = input('輸入動作:')
    if q == '1':
      print('選擇材料種類種類')
      print('主')
      print('a 豬肉')
      print('\n副')
      print('b 胡蘿蔔  c 荸薺  d 薑  e 蔥')
      print('\n調味(1)')
      print('f 胡椒粉  g 味精  h 太白粉')
      print('i 鹽  j 香油  k 醬油  l 酒')
      print('\n調味(2)')
      print('m 太白粉  n 麵粉')
      w=input('輸入代號:')
      if w=='a':
        a = input('輸入克數:')
        l1.pop()
        l1.insert(1, a + 'g')
        aa = input('刀工:')
        l1.pop()
        l1.insert(2, '刀工:' + aa)
      elif w=='b':
        b = input('輸入克數:')
        l2.pop()
        l2.insert(1, b + 'g')
        bb= input('刀工:')
        l2.pop()
        l2.insert(2, '刀工:' + bb)
      elif w=='c':
        c = input('輸入克數:')
        l3.pop()
        l3.insert(1, c + 'g')
        cc = input('刀工:')
        l3.pop()
        l3.insert(2, '刀工:' + cc)
      # elif w=='b':
      #   a = input('輸入克數:')
      #   l1.pop()
      #   l1.insert(1, a + 'g')
      #   aa = input('刀工:')
      #   l1.pop()
      #   l1.insert(2, '刀工:' + aa)
      # elif w=='b':
      #   a = input('輸入克數:')
      #   l1.pop()
      #   l1.insert(1, a + 'g')
      #   aa = input('刀工:')
      #   l1.pop()
      #   l1.insert(2, '刀工:' + aa)
      # elif w=='b':
      #   a = input('輸入克數:')
      #   l1.pop()
      #   l1.insert(1, a + 'g')
      #   aa = input('刀工:')
      #   l1.pop()
      #   l1.insert(2, '刀工:' + aa)
      # elif w=='b':
      #   a = input('輸入克數:')
      #   l1.pop()
      #   l1.insert(1, a + 'g')
      #   aa = input('刀工:')
      #   l1.pop()
      #   l1.insert(2, '刀工:' + aa)
      # elif w=='b':
      #   a = input('輸入克數:')
      #   l1.pop()
      #   l1.insert(1, a + 'g')
      #   aa = input('刀工:')
      #   l1.pop()
      #   l1.insert(2, '刀工:' + aa)
      # elif w=='b':
      #   a = input('輸入克數:')
      #   l1.pop()
      #   l1.insert(1, a + 'g')
      #   aa = input('刀工:')
      #   l1.pop()
      #   l1.insert(2, '刀工:' + aa)
      # elif w=='b':
      #   a = input('輸入克數:')
      #   l1.pop()
      #   l1.insert(1, a + 'g')
      #   aa = input('刀工:')
      #   l1.pop()
      #   l1.insert(2, '刀工:' + aa)
      # elif w=='b':
      #   a = input('輸入克數:')
      #   l1.pop()
      #   l1.insert(1, a + 'g')
      #   aa = input('刀工:')
      #   l1.pop()
      #   l1.insert(2, '刀工:' + aa)

    if q=='2':
      print(l1)
      print(l2)
      print(l3)
      print(l4)
      print(l5)
      print(l6)
      print(l7)
      print(l9)
      print(l10)
      print(l12)
      print(l13)
      print(l14)
      print(l8)