# 辞書をfor文で処理をする

d = {'x': 100, 'y': 200}

print(d.items())

for k, v in d.items():
    print(k, ':', v)