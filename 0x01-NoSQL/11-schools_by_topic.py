#!/usr/bin/env python3
"""
MongoDB School Search Module

This module provides a function to find all schools
in a MongoDB collection that have a specific topic.
"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Finds and returns a list of all schools that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for in the school's topics.

    Returns:
        A list of documents (schools) that contain the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))
