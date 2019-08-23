telebook = dict()
match = [str(x) for x in range(1,6)]

while 1:
    print('''
*******歡迎使用通訊錄*******
          
1、建立一個新的聯絡人
2、以人名查詢電話
3、以電話查詢人名
4、列出整份通訊錄
5、退出程式''')
    choose = input('請做出您的選擇：')
    while 1:
        if choose in match:
            break
        else:
            choose = input('選擇錯誤，請重新輸入(1~5)：')
    if choose == '1':
        print('開始建立新的聯絡人',end="")
        name = input('請輸入姓名：')
        phone = input('請輸入電話：')
        telebook[name] = phone
        print(f'新的聯絡人「{name}」的電話「{phone}」已經新增到通訊錄')
        
    elif choose == '2':
        print('以人名查詢電話',end="")
        name = input('請輸入姓名，我幫您查電話：')
        phone = telebook.get(str(name), '不好意思，通訊錄裡面查無該人電話')
        print(f'搜尋結果：「{phone}」')
        
    elif choose == '3':
        retelebook = {x:y for y,x in telebook.items()}
        print('以電話查詢人名',end="")
        phone = input('請輸入電話，我幫您看看是誰的號碼：')
        name = retelebook.get(str(phone), '不好意思，通訊錄裡面查無該電話')
        print(f'搜尋結果：「{name}」')

    elif choose == '4':
        print('列出整份通訊錄')
        count = 1
        for i,j in telebook.items():
            print(f'{str(count)}、「{str(i)}」的電話號碼為：{str(j)}')
            count += 1
    elif choose == '5':
        print('感謝使用本程式，歡迎再次使用')
        break       
    go = input('是否要繼續使用本程式(輸入n退出)？')
    if go == 'n':
        print('感謝使用本程式，歡迎再次使用')
        break