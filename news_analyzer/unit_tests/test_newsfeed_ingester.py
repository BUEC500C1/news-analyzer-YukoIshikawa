from newsfeed_ingester import *
import pytest

def test_convert_length():
  ## correct cases 
  assert convert_length(100, "meter", "feet") == 328.08
  assert convert_length(8, "meter", "inches") == 314.96
  assert convert_length(2000, "meter", "mile") == 1.24
  assert convert_length(56, "feet", "meter") == 17.07
  assert convert_length(14, "inch", "meter") == 0.36
  assert convert_length(90, "mile", "meters") == 144927.54
  ## error cases 
  assert convert_length("456", "meters", "feets") == "Error: Invalid input"
  assert convert_length(5, "mm", "inches") == "Error: Invalid input"
  assert convert_length(45, "meters", "mille") == "Error: Invalid input"
  assert convert_length(12, "ft", "meters") == "Error: Invalid input"
  assert convert_length(78, "meter", "inch") == "Error: Invalid input"
  assert convert_length(5, "ichhhh", "meter") == "Error: Invalid input"
  assert convert_length(43, "mille", "meter") == "Error: Invalid input"
  assert convert_length(89, "cm", "inches") == "Error: Invalid input"
  assert convert_length("-123", "meters", "feet") == "Error: Invalid input"
  assert convert_length(345, "meters", "million") == "Error: Invalid input"
  
def test_convert_weight():
  ## correct cases 
  assert convert_weight(10, "kilogram", "pound") == 22.05
  assert convert_weight(5, "kilogram", "ounce") == 176.35
  assert convert_weight(67, "pound", "kilogram") == 30.39
  assert convert_weight(12, "ounce", "kilogram") == 0.34
  ## error cases 
  assert convert_weight("string", "kilogram", "pound" ) == "Error: Invalid input"
  assert convert_weight(0, "kilogram", "Pond" ) == "Error: Invalid input"
  assert convert_weight(12, "mmgram", "ounce" ) == "Error: Invalid input"
  assert convert_weight(36, "ounce", "kilogram" ) == "Error: Invalid input"
  assert convert_weight(45, "ounce", "L" ) == "Error: Invalid input"
  assert convert_weight(0, "pound", "ounce" ) == "Error: Invalid input"
  
def test_convert_temperature(): 
  ## correct cases 
  assert convert_temperature(0, "celcius", "fahrenheit") == 32.00
  assert convert_temperature(122, "fahrenheit", "celcius") == 50.00 
  ## error cases 
  assert convert_temperature("string", "celcius", "fahrenheit") == "Error: Invalid input"
  assert convert_temperature(40, "cel", "fahrenheit") == "Error: Invalid input"
  assert convert_temperature(23, "cel", "fahrennnnn") == "Error: Invalid input"
