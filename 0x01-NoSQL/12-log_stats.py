#!/usr/bin/env python3
"""
Nginx log stats module

This script connects to a MongoDB database and prints statistics about the
Nginx logs stored in the 'logs.nginx' collection.
"""

from pymongo import MongoClient


def log_stats():
    """Provides statistics about Nginx logs stored in MongoDB."""
    # Connect to the MongoDB server
    client = MongoClient()
    # Access the database and collection
    db = client.logs
    nginx_collection = db.nginx

    # Count total number of documents in the collection
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count the occurrences of each method in the logs
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count documents where method is GET and path is /status
    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")


if __name__ == "__main__":
    log_stats()
