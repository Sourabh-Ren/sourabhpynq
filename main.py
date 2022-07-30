from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/update/<int:sno>', methods=['GET','POST'])
# def update(sno):
#     res = {
#         "num":sno
#     }
#     return res

# @app.route('/postsend', methods=['GET','POST'])
# def postsend():
#     if request.method=="POST":
#         email = request.form.get('email')
#         password = request.form.get('password')
#         res = {
#             "email": email,
#             "password": password
#         }
#         return res

@app.route('/querydata', methods=['GET','POST'])
def querydata():
    if request.method=="GET":
        temp = request.args.get('temp')
        humi = request.args.get('humi')
        res = {
            "temp": temp,
            "humi": humi
        }
        return res

# @app.route('/postsendjson', methods=['GET','POST'])
# def postsendjson():
#     if request.method=="POST":
#         data = request.get_json()
#         return data

if __name__ == "__main__":
    app.run(debug=True, port=8000)