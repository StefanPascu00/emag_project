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
    if user in users.keys():
        if passwd == users[user]:
            data = emag_db.read_products(config=config)
            return render_template("home.html", data=data)

    return render_template("login.html")

@app.route("/delog")
def delog():
    return render_template("login.html")


if __name__ == '__main__':
    app.run()