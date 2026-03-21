import pytest
from waf_lite import is_suspicious

def test_classic_injections():
    
    assert is_suspicious("' OR 1=1 --") == True
    assert is_suspicious('" OR 1=1 --') == True
    assert is_suspicious("admin' --") == True

def test_sql_keywords():
    
    assert is_suspicious("SELECT * FROM users") == True
    assert is_suspicious("union select password from admins") == True

def test_special_characters():
    
    assert is_suspicious("search; DROP") == True
    assert is_suspicious("some text -- comment") == True