from flask import Flask, render_template, request

import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/newstudent")
def new_student():
    return render_template('student.html')


@app.route("/addstudent", methods=['POST', 'GET'])
def addstudent():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect("database.db") as connection:
                my_cursor = connection.cursor()
                my_cursor.execute("INSERT INTO students (name, addr, city, pin) VALUES (?,?,?,?)", (name, address, city,
                                  pin))
                msg = "Record Successfully inserted"
        except:
            connection.rollback()
            msg = "Error inserting operations"
        finally:
            return render_template("result.html", msg=msg)
            connection.close()


@app.route("/list")
def list():
    connection = sql.connect("database.db")
    connection.row_factory = sql.Row
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT * FROM students")
    rows = my_cursor.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
