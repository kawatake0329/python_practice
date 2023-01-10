# ラムダ

l = ['Mon', 'tue', 'Wed', 'Tue', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()
# 上記のものをラムダを使って一行にて行う上の行はwordに入ったものを先頭のものを大文字に変換してくれる

# sample_func = lambda word: word.capitalize

# 更に下記の内容にラムダを入れることで更に入れることが出来る！
change_words(l, lambda word: word.capitalize)

# ラムダの必要性は、他のcapitalize以外の物を使う際等かさばってしまう時に使う！