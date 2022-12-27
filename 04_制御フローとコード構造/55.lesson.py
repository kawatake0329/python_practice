# 関数内関数

# 使い道は関数内で何度も関数を使う場合(他の場面で使うことのない)今回のファンクションが使える！
def outer(a, b):
    
    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)