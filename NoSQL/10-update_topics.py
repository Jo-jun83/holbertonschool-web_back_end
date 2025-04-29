#!/usr/bin/env python
"""Module to update the topics of a document in
a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a document in a MongoDB collection.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
