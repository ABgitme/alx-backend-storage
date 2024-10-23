#!/usr/bin/env python3
import redis
import uuid
from typing import Union
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve data from Redis.
            fn (Optional[Callable]): A callable used to convertthe
            data back to the desired format.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data
            in its original or converted format.
        """
        # Get the data from Redis
        data = self._redis.get(key)

        # If the key does not exist, return None
        if data is None:
            return None

        # If a conversion function is provided, apply it
        if fn:
            return fn(data)

        # Otherwise, return the raw data (as bytes)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The key to retrieve data from Redis.

        Returns:
            Optional[str]: The retrieved string,
            or None if the key doesn't exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The key to retrieve data from Redis.

        Returns:
            Optional[int]: The retrieved integer,
            or None if the key doesn't exist.
        """
        return self.get(key, fn=int)
