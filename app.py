from flask import Flask, request
import requests

app = Flask(__name__)

url = "https://dummyjson.com/products"

@app.route("/", methods=['GET'])
def view_products():
    response = requests.get(url)
    data = response.json()

    return data

@app.route("/<id>", methods=['GET'])
def search_products(id):
    response = requests.get(f"{url}/{id}")
    data = response.json()

    return data

@app.route("/s", methods=['GET'])
def view_search_products():
    limit = request.args.get("limit")
    skip = request.args.get("skip")
    select = request.args.get("select")

    response = requests.get(f"{url}?limit={limit}&skip={skip}&select={select}")
    data = response.json()
    
    return data

if __name__ == "__main__":
    app.run(debug=True)