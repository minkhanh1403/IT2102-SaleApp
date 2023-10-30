from flask import Flask, render_template, request
import  dem

app = Flask(__name__)

@app.route('/')
def index():
    kw = request.args.get('kw')

    cates = dem.load_categories()
    products = dem.load_products(kw=kw)

    return  render_template('index.html',cate = cates, product = products)

@app.route('/products/<id>')
def details(id):
    return render_template('details.html')

if __name__ == '__main__':
    app.run(debug=True)
