#!/usr/bin/python3
"""
index module
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    status route
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)
