


from flask import Flask , jsonify , request


app = Flask(__name__)


todo = [

    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    },

    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
    },
]

@app.route('/')
def hello_world():
    return 'Hello, world!,from Ronak'



@app.route('/add-data', methods = ["POST"])

def add_data(): 
    todos = {
        'id': todo[-1]['id'] + 1,
        'name': request.json['name'],
        'username': request.json['username'],
        'email':request.json['email']
        # 'email': request.json.get('email',"")
    }

    todo.append(todos)
    return jsonify({
        'status': 'success',
        'message':'USER added successfully'
    })
     

@app.route('/get-data')
def get_data():
    return jsonify({
        'RETURNED DATA':todo
    })


if (__name__ == "__main__"):
    app.run(debug=True)


