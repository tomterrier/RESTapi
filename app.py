#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:07:59 2020

@author: tomter
"""


from flask import Flask
from flask_restful import Api #flask_restful is such that it accepts to return a dictionnary (no need to jsonify)
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister

from resources.item import Item, ItemsList

from resources.store import Store, StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'bigt'
api=Api(app)


jwt=JWT(app, authenticate, identity)


#get() and post() have to have the same signature because they are both defined in the same class, which is then added to the api through api.add_resource(.....)

    
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app) 
    app.run(port=5000, debug=True) #debug = True allows to be understand the errors much better 