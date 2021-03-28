from flask import Flask, request, json, jsonify
from app import * 

def test_index():
    assert index() == {'message': 'Welcome to my Resst API!'}

def test_list_all_files():
    assert list_all_files() == {
  "message": {
    "1": "Thanksgiving Advice for BU Students: Stick Around, Have a Safe Friendsgiving", 
    "2": "ENG’s David Bishop Tapped as Member of National Academy of Engineering"
  }
}

def test_show_file():
    assert show_file(1) == {
  "message": "Thanksgiving Advice for BU Students: Stick Around, Have a Safe Friendsgiving"
}
    assert show_file(2) == {
  "message": "ENG’s David Bishop Tapped as Member of National Academy of Engineering"
}
    
def test_delete_file():
    assert delete_files(1) == {
  "message": "Thanksgiving Advice for BU Students: Stick Around, Have a Safe Friendsgiving"
}
    assert delete_files(2) == {
  "message": "ENG’s David Bishop Tapped as Member of National Academy of Engineering"
}
  
def test_create_file():
    assert create_file() == {
  "message": {
    "1": "Thanksgiving Advice for BU Students: Stick Around, Have a Safe Friendsgiving", 
    "2": "ENG’s David Bishop Tapped as Member of National Academy of Engineering"
  }
}

def update_file(fileid):
    assert delete_files(1) == {
  "message": "Thanksgiving Advice for BU Students: Stick Around, Have a Safe Friendsgiving"
}
    assert delete_files(2) == {
  "message": "ENG’s David Bishop Tapped as Member of National Academy of Engineering"
}
