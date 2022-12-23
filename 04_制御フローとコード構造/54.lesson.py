# Docstrings とは

# 例をそのまま持ってきた説明ようにfunction等を使う際はダブルクォーテーションを使って書く

def example_func(param1,param2):
    """Example function with types documented in the docstring.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    
    Returns:
        bool: The return value. True for success, False otherwise.
    
    """
    print(param1)
    print(param2)
    return True

# この記述を使うことで説明がターミナルに出てくるようにできる！
print(example_func.__doc__)