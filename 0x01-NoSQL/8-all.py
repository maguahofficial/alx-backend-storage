#!/usr/bin/env python3
""" 
the Python function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    this function lists all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
