# 例外処理

l = [1, 2, 3]
i = 5
del l

try:
    l[i]
except IndexError as exc:
    print("Don't worry: {}".format())
except NameError as ex:
    print(ex)
# exception = 例外
except Exception as ex:
    print('other:{}'.format(ex))

finally:
    print("last")