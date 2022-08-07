#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""models/__init__.py - setup db engine"""


storage = FileStorage()
storage.reload()
