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
      l_lobo.append(l+'g')
      if l in l_lobo:
        continue
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
# juice_list = ["1", "2"]
# while True:
#     print("1  想加入菜單的果汁")
#     print("2  顯示菜單")
#     print("3  結束程式")
#     a = input("選擇步驟:")
#     if a == "1":
#         new = input("輸入果汁:")
#         if new in juice_list:
#           print("已有此果汁")
#         else:
#           juice_list.append(new)
#           print("新增完成")
#          for l in juice_list:
#             if new == l:
#                 print("已有此果汁")
#                  break
#          else:
#              juice_list.append(new)
#              print("新增完成")
#     if a == "2":
#         print(juice_list)
#     if a == "3":
#         print("結束程式")

