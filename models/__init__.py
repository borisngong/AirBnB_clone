#!/usr/bin/python3
"""Module for initializes the package"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
