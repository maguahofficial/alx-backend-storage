#!/usr/bin/env python3
"""
the python function that changes all topics of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    this function updates many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
