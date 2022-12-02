# while文とcontinue文とbreak文
count = 0

# countが5を超えるとシステムがストップする
while count < 5:
    print(count)
    count += 1
# そのため、一つ上の行countを間違った形にしてしまうと無限ループが起こる

# break文を使った方法
count = 1
while True:
    if count >= 5:
        break
    
    if count == 2:
        count += 1
        continue
#上記のようにbreakではなくcontinueを使うとその処理だけ飛ばしてくれるようになる
# 今回は2の時表示をせず次の3から表示されるようになる。 

    print(count)
    count += 1
