# while else文

count = 0

while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
# elseを使うことでwhile文を抜けた際に下記のようにdoneを表示させることが出来る
# またbreakを使ってループから抜けなければelseが使われる
else:
    print('done')