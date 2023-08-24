from werkzeug.serving import run_simple
from flask import Flask,request
import json


app= Flask(__name__)
    
products=[
    {
        "id": 1,
        "name": "Product 1",
        "price": 29.99,
        "category": "Electronics",
        "color": ["Black", "Silver", "White"]
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 19.99,
        "category": "Clothing",
        "color": ["Red", "Blue", "Green"]
    },
    {
        "id": 3,
        "name": "Product 3",
        "price": 9.99,
        "category": "Toys",
        "color": ["Yellow", "Purple"]
    }
]
def filter_product(query_args,products):
    filtered_list = []
    for key,value in query_args:
        for product in products:
            if product[key] == value:
                filtered_list.append(product)
    return filtered_list

    

def get_user_list():
    with open('repo/userdata.json',"r") as file:
        data = file.read()
    return json.loads(data)

@app.route('/user/<username>')
def get_username(username):
    return list(filter(lambda user:user.get("name")==username,get_user_list() ))

@app.route('/product')
def get_product():
    if len(request.args):
        return filter_product(request.args.items(), products)
    return products



@app.route('/product/<int:id>')
def get_product_by_id(id):
    return list(filter(lambda product:product.get("id") == id,products))

@app.route('/product/<int:id>/<key>')
def get_product_color(id, key):
    return list(filter(lambda product:product.get("id") == id,products))[0].get(key)

@app.route('/product/<int:id>/color/<int:index>')
def get_product_color_by_id(id, index):
    try:
        return list(filter(lambda product:product.get("id") == id,products))[0].get("color")[index - 1]
    except IndexError:
        return [], 404#BAD REQUEST
    
@app.route('/user')
def get_user():
    return get_user_list()




if __name__ == "__main__":
    run_simple('localhost', 5000, app, use_reloader=True)