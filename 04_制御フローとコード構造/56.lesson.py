#  クロージャー

# 今の段階では難しい物らしいので雰囲気だけ理解！デベロッパーで動きを見ると分かりやすいかも！

def outer(a, b):
    
    def inner():
        return a + b
    return inner

f = outer(1, 2)
r = f()
print(r)

# 円を求める場合

def circle_area_func(pi):
    def circle_area(radius):#半径
        return pi * radius * radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

# 設定した引数を元にして後の用途で使い分ける事をイメージする
# 大まかに変数の関数版かな？