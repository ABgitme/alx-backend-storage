#!/usr/bin/env python3
"""
MongoDB Collection Listing Module
This module provides a function to
list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of all documents in the collection.
        Returns an empty list if no documents are found.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
