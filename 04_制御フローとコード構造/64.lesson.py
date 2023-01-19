"""
Test Test ################################
"""

animal = 'cat'


def f():
    """Test func doc"""
    print(f,__name__)
    print(f,__doc__)



def f():
    global animal
    animal = 'dog'
    print('local', locals())

f()
print('global:', globals())