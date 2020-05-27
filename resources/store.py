from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(name):
        store = StoreModel.find_by_name(name)
        if store : 
            return store.json()
        return {'message': 'store not found'}, 404
    
    def post(name):
        store = StoreModel.find_by_name()
        if store:
            return {'message' : 'store already exists'}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'an error occured'}
        return store.json(), 201
    
    def delete(name):
        store = StoreModel.find_by_name()
        if store:
            store.delete_from_db()
        return {'message': 'store deletion occured'}
    
    
class StoreList(Resource):
    def get():
        return {'stores' : [store.json() for store in StoreModel.query.all()]}