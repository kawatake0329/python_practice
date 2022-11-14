s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print("##################")

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike','Nancy'))

# 14.15.レッスン開始 

# python 3.6からf-stringsが使えるようになった14でのレッスンで習ったことが簡単に出来るようになっているこちらのほうを覚える

a = 'a'
print(f'a is {a}')

x,y,z =1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My nmae is {name} {family}. Watashi ha {family} {name}')