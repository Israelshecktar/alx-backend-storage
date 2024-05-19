#!/usr/bin/env python3
"""
Module to return list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic

    Args:
    mongo_collection: pymongo collection object
    topic (string): topic searched

    Returns:
    List of documents containing the topic
    """
    return list(mongo_collection.find({ "topics": topic }))
