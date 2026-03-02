#!/usr/bin/env python3
"""
Change all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (list of str): list of topics to set
    """
    mongo_collection.update_many(
        {"name": name },
        {"$set": {"topics": topics} }
    )
