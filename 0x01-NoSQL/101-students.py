#!/usr/bin/env python3
"""a Python function that returns all students sorted by average score:"""


def top_students(mongo_collection):
    """ all student sorted by average score"""
    all = mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
    return all
