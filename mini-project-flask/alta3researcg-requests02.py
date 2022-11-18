#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/about', methods=['GET'])
def ReturnJSON():
    if (request.method == 'GET'):
        data = {
            "Authors": "Number of Authors",
            "Number of Posts": 2,
        }

        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
