from flask import Flask, render_template, request
import emag_db

app = Flask(__name__)
config = emag_db.read_config()
user_id, username, password = emag_db.read_admins(config=config)

users = {
    username: password
}




@app.route("/test")
def second_func():
    print("S-a rulat cand apasam pe link")
    return render_template("test.html")


@app.route("/")
def first_func():
    print("S-a rulat cand apasam pe link")
    return render_template("login.html")


@app.route("/login", methods=['POST'])
def web_login():
    user = request.form['username']
    passwd = request.form['password']
    # if user in users.keys():
    #     if passwd == users[user]:
    data = emag_db.read_products(config=config)
    return render_template("home.html", data=data)

    # return render_template("login.html")


@app.route("/log_out")
def delog():
    return render_template("login.html")


@app.route("/add_products", methods=['POST', 'PUT'])
def add_products():
    # ca sa vad ce tip de request e, apelez request.method
    try:
        product_name = request.form['product_name']
        store = request.form['store']
        price = request.form['price']
        query = (f"INSERT into emag.products(name, store, price) "
                 f"values ('{product_name}', '{store}', {price})")
        emag_db.execute_query(sql_query=query, config=config)
        data = emag_db.read_products(config=config)
        return render_template("home.html", data=data)
    except Exception as e:
        return {"ERROR": f"404 NOT FOUND {e}"}


if __name__ == '__main__':
    app.run()
# diesz id punct clasa