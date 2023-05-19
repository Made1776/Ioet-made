import pytest
from    verificacion_de_parentesis  import check_parentheses

def test_verificacion_de_parentesis ():
    stack = "()[]{}" #A1
    except_Result = True
    stack = check_parentheses(stack) #A2
    assert stack == except_Result #A3
    
