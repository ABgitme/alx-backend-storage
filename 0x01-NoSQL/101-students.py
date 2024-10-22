#!/usr/bin/env python3
"""
MongoDB Student Statistics Module

This module provides a function to return all
students from a MongoDB collection,
sorted by their average score.
The average score is added as a field in the output.
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of students sorted by average score in descending order,
        with each item containing the average
        score under the key 'averageScore'.
    """
    # Calculate average score for each student and sort by it
    students = mongo_collection.aggregate([
        {
            # Unwind the array to process each topic separately
            "$unwind": "$topics"
        },
        {
            # Group by student, accumulate the total score and count the topics
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            # Sort by average score in descending order
            "$sort": {"averageScore": -1}
        }
    ])

    return list(students)
