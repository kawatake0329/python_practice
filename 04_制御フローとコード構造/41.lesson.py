# input関数
while True:
# 下記のinputを使うことで入力をすることが出来今回は
# okが入力されるまでループから抜けないようになっている
    word = input('Enter:')
    if word == 'ok':
        break
    print('next')