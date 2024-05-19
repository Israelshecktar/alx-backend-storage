#!/usr/bin/env python3
"""
Module to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
    mongo_collection: pymongo collection object

    Returns:
    A list of all documents in the collection   """
    return list(mongo_collection.find())
