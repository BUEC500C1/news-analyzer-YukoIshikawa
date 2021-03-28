from nlp_analyzer import *
import pytest

def test_analyze_sentiment():
    assert analyze_sentiment("sample.txt") == "-1" 
    return sentiment_score
	
def test_analyze_entities():
    assert analyze_entities("sample.txt") == "Location"
 	