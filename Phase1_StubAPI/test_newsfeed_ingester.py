from newsfeed_ingester import *
import pytest

def test_search_keyword():
    assert search_keyword("Sunny") == "Today is a good day"

def test_search_sentiment():
    assert search_sentiment("positive") == "I'm happy"
    
def test_search_date():
    assert search_date("something") == "Today is an election day"
    