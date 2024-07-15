#!/usr/bin/env python3
"""
 the python function that inserts a new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    ths function insert into school
    """
    return mongo_collection.insert_one(kwargs).inserted_id
