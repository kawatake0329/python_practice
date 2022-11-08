num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
# 上記のように代入する量が多いと、見ずらくなってしまうので下記のように別々に代入することが望ましい
a = 'Mike'
b = '1'

# i と j を入れ替える場合
i = 10
j = 20
tmp = i
i = j
j = tmp

print(i, j)

# i と j を入れ替える場合(更に簡単に)
a = 100
b =200
print(a, b)
# この一行で完結
a, b = b, a
print(a, b)