""" Test for merge strings alternatively 
""" 
import pytest

def join_lists(list_a, list_b):
    """Join two lists by alternating the characters

    Args:
        list_a (_type_): lists must be made of lower case letters of a length between 1 and 100 
        list_b (_type_): lists must be made of lower case letters of a length between 1 and 100

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    len_a = len(list_a)
    len_b = len(list_b)
    
    if len_a < 1:
        raise ValueError("List A is is less than 1")
    
    if len_b < 1:
        raise ValueError("List B is is less than 1")
    
    if len_a > 100:
        raise ValueError("List A is is greater than 100")
    
    if len_b > 100:
        raise ValueError("List B is is greater than 100")
    
    for a in list_a:
        if (a.isalpha() is False or a.islower() is False):
            raise ValueError("List A must only contain lower case letters")
    
    for b in list_b:
        if (b.isalpha() is False or b.islower() is False):
            raise ValueError("List B must only contain lower case letters")
   

    # start to iterate though the lists at zero
    # and prepare to output an array as a result
    i = 0
    j = 0
    result = []
    
    # What needs to be determined is whether or not the arrays are 
    # equal in size. If not, the smaller one will be the outer loop
    # and then the remainder if thelarger array will be appended to 
    # the result
    #primary = []
    remainder = []
    max = 0
    is_same_size = len_a == len_b
    
    if is_same_size is True:
        common = len_a
    elif len_a > len_b:
        common = len_b
        max = len_a
        remainder = list_a
    else:
        common = len_a
        max = len_b
        remainder = list_b
    
    # Iterate though the lists alternating adding a character from
    # the first list and a character from the second list while the sizes
    # are equal
    while i < common:
        result.append(list_a[i])
        result.append(list_b[i])
        i += 1
    
    # Optionally, take care of the remainder
    if is_same_size is False:
        j = common 
        while j < max:
            result.append(remainder[j])
            j += 1
        
    return result
    
    
def test_equal_size_words():
    """ Test basics """  
    word1 = "abc"
    word2 = "def"

    letters1 = list(word1)
    letters2 = list(word2)
    
    assert len(letters1) == 3
    assert len(letters2) == len(letters1)
    assert letters1[0] == "a"
    assert letters2[2] == "f"
    
    result = join_lists(letters1, letters2) 
    expected = ["a","d","b","e","c","f"]
    
    assert result == expected
    assert len(result) == len(letters1) + len(letters2)
    
def test_lhs_is_larger():
    word1 = "abcd"
    word2 = "efg"
    
    letters1 = list(word1)
    letters2 = list(word2)
    
    result = join_lists(letters1, letters2) 
    expected = ["a","e","b","f","c","g", "d"]
    
    assert result == expected
    assert len(result) == len(letters1) + len(letters2)
    
def test_rhs_is_larger():
    word1 = "abc"
    word2 = "defg"
    
    letters1 = list(word1)
    letters2 = list(word2)
    
    result = join_lists(letters1, letters2) 
    expected = ["a","d","b","e","c","f", "g"]
    
    assert result == expected
    assert len(result) == len(letters1) + len(letters2)
    
def test_lhs_has_caps():
    
    word1 = "Abc"
    word2 = "def"
    
    letters1 = list(word1)
    letters2 = list(word2)
    
    with pytest.raises(ValueError, match='List A must only contain lower case letters'):
        result = join_lists(letters1, letters2)
    
def test_rhs_has_caps():
    
    word1 = "abc"
    word2 = "dEf"
    
    letters1 = list(word1)
    letters2 = list(word2) 
    
    with pytest.raises(ValueError, match='List B must only contain lower case letters'):
        result = join_lists(letters1, letters2)
        result.