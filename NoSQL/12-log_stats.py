#!/usr/bin/env python3
"""This script connects to a MongoDB database, retrieves log statistics
from an 'nginx' collection, and prints the results."""
import pymongo


def print_logs():
    """Connects to the MongoDB 'nginx' collection, retrieves log statistics,
    and prints the total number of logs, counts of HTTP methods, and
    status checks."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    collection = client.logs.nginx

    logs = collection.count_documents({})
    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    status = collection.count_documents({"method": "GET", "path": "/status"})

    print("{} logs".format(logs))
    print("Methods:")
    print("\t method GET: {}".format(get))
    print("\t method POST: {}".format(post))
    print("\t method PUT: {}".format(put))
    print("\t method PATCH: {}".format(patch))
    print("\t method DELETE: {}".format(delete))
    print("{} status check".format(status))


print_logs()
