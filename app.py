# YOUR FLASK APP HERE
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import datetime # adds timestamps to database entries
import pprint # pretty print notation
app = Flask(__name__)
app.config['DEBUG'] = True
# if using flask run, run in command line: export FLASK_DEBUG=0

# To point at a server
host = 'localhost'
port = 27017
client = MongoClient(host, port)

db = client.test_database

ops_collection = db.operators
loops_collection = db.loops

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loops')
def loops():
    return render_template('loops.html', loops=loop_sections)

@app.route('/operators', methods=['GET', 'POST'])
def operators():
    if request.method=='POST':
        return render_template('pie.html', operators=operator_sections)
    else:
        return render_template('operators.html', operators=operator_sections)



floor_division = {
    "name": "Floor Division",
    "description": "Division that rounds down to the nearest integer. Also known as integer division.",
    "symbol": "//",
    "example": "3 // 2 == 1",
    "uses": "A common situation we might see this operator is when we need to calcuate a list index, which will need to be a whole number. For example, perhaps we are trying to find the middle index of a list, but there are an even number of elements. In this case, we could use floor division to select the leftmost element in the list by default."
}

exponent = {
    "name": "Exponent",
    "description": "Performs exponential (power) calculation on operators",
    "symbol": "//",
    "example": "a**b =10 to the power 20",
    "uses": "A common situation we might see this operator is when we need to use powers of ten in large data sets. The power operator can be useful in applying powers of 10 in calculations."
}

in_operator = {
    "name": "In",
    "description": "Evaluates to true if it finds a variable in the specified sequence and false otherwise.",
    "symbol": "//",
    "example": "x in y, here in results in a 1 if x is a member of sequence y.",
    "uses": "Membership operators like the in operator test for membership in a sequence, such as strings, lists, or tuples."
}

for_in_loops = {
    "name": "For-In Loops",
    "description": "It has the ability to iterate over the items of any sequence, such as a list or a string.",
    "example": "for iterating_var in sequence: statements(s)",
    "uses": "For-In Loops are used to iterate over large objects, often containing many items. You may find them particularly useful for manipulating large data sets"
}

while_loops = {
    "name": "While Loops",
    "description": "Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.",
    "example": "while expression: statement(s)",
    "uses": "The condition in a while loop may be any expression, and true is any non-zero value. The loop iterates while the condition is true. When the condition becomes false, program control passes to the line immediately following the loop. A while loop becomes infinite loop if a condition never becomes FALSE. You must use caution when using while loops because of the possibility that this condition never resolves to a FALSE value. This results in a loop that never ends. Such a loop is called an infinite loop."
}

operator_sections = [floor_division, exponent, in_operator]
loop_sections = [for_in_loops, while_loops]

ops_collection.insert_many([floor_division, exponent, in_operator])


# __main__ is similar to the index.js in javascript/express
if __name__ == '__main__':
    app.run()