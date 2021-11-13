from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)


# @app.route('/concatenation/<string:name>/<int:age>')
# def concat_variables(name: str, age: int):
#     return jsonify(name + str(age))


@app.route('/concatenation')
def with_parameters():
    message_string = request.args.get('message_string')
    message_id = int(request.args.get('message_id'))
    print("response "+message_string+str(message_id))
    return message_string + str(message_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3001)))