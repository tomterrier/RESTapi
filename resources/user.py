#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:39:53 2020

@author: tomter
"""
from flask_restful import Resource, reqparse
from models.user import UserModel
    

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required = True,
        help = 'Field cannot be blank'
    )
    parser.add_argument('password',
        type=str,
        required = True,
        help = 'Field cannot be blank'
    )
    
    def post(self):
        data=UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {'message': 'user with that username already exists'}
        
        user=UserModel(data['username'],data['password']) #userModel(**data)
        user.save_to_db()
        
        return { "message": "User created succesfully"}, 200
    
    
    
    