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


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    returns count of all class objects
    """
    if request.method == 'GET':
        response = {}
        classes_d = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in classes_d.items():
            response[value] = storage.count(key)
        return jsonify(response)
