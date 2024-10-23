#!/usr/bin/env python3
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to interact with Redis and
    store data with randomly generated keys.

    Methods:
        __init__: Initializes Redis connection and flushes the database.
        store: Stores data in Redis with a randomly
        generated key and returns the key.
    """
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]):
            The data to store in Redis.

        Returns:
            str: The generated key where the data is stored.
        """
        # Generate a random UUID as the key
        key = str(uuid.uuid4())

        # Store the data in Redis using the key
        self._redis.set(key, data)

        # Return the key
        return key
