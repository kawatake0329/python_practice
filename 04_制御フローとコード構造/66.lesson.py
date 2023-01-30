# 独自例外の作成

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
# 上記のようにraise　UpppercaseError　を作ることで
# 自分独自の例外を作りチェックすることが可能となる

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')

# UppercaseErrorの部分は変えることは可能だが
# valueErrorのように既存のものを使うと
# 他のエンジニアに誤解を生ませてしまうので
# 独自のエラー命名をすることが好ましい