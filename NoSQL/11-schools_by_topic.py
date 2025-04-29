#!/usr/bin/env python3
"""
This module provides a function to query a MongoDB collection
and retrieve all documents that contain a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Queries a MongoDB collection to retrieve all documents
    that contain a specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
