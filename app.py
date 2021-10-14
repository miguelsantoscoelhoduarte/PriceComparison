from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from main import get_all_products_by_string_fnac, get_all_products_by_string_worten, product_list_to_json

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')
app.config['SECRET_KEY'] = 'ines'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('./index.html')

@app.route('/AllFnacProducts/<search_string>')
def AllFnacProducts(search_string):
	all_fnac_products = get_all_products_by_string_fnac(search_string)
	return product_list_to_json("output", all_fnac_products)

@app.route('/AllWortenProducts/<search_string>')
def AllWortenProducts(search_string):
	all_worten_products = get_all_products_by_string_worten(search_string)
	return product_list_to_json("output", all_worten_products)


if __name__ == '__main__':
	socketio.run(app, debug=True)
