#!/usr/bin/env python3
"""
MongoDB Document Insertion Module

This module provides a function to
insert a new document into a MongoDB collection.
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs representing the fields of the document.

    Returns:
        The _id of the inserted document.
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id
