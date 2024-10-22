#!/usr/bin/env python3
"""
Log Stats Module

This script provides statistics about Nginx logs
stored in a MongoDB collection.
It outputs the total number of logs,
the count of requests by method, and the top 10 IPs.
"""

from pymongo import MongoClient


def print_log_stats():
    """Fetch and print statistics from the Nginx logs collection."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Count total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count requests by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count status check
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Get the top 10 IPs
    print("IPs:")
    ip_counts = nginx_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",  # Group by IP
                "count": {"$sum": 1}  # Count occurrences
            }
        },
        {
            "$sort": {"count": -1}  # Sort by count in descending order
        },
        {
            "$limit": 10  # Get the top 10 IPs
        }
    ])

    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    print_log_stats()
