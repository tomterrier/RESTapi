#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:32:35 2020

@author: tomter
"""
from models.user import UserModel


def authenticate(username, password):
    user=UserModel.find_by_username(username)
    if user and user.password== password:
        return user
    
def identity(payload):
    user_id=payload['identity']
    return UserModel.find_by_id(user_id)