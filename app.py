from flask import Flask, jsonify

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'description':'Pedido de Compra 1',
        'Items':[
            {
                'id':1,
                'description':'Item do pedido 1',
                'price':20.99
            }
        ]
    }
]



@app.route('/')
def home():
    return "Hello World!"

@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)


@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id):
    for pedido in purchase_orders:
        if pedido['id'] == id:
            return jsonify(pedido)
    return jsonify({'Message': 'Pedido {}, não encontrado!'.format(id)})


app.run(port=5000)