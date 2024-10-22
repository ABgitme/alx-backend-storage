#!/usr/bin/env python3
"""
MongoDB Document Update Module

This module provides a function to update the topics
of a school document in a MongoDB collection.
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of all school documents
    where the name matches.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The school name to update.
        topics (list of str): The list
        of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
