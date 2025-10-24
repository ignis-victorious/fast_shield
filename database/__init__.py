

"""
 : Database Package

This folder contains all our database-related code.
For Starters:
- Right now we use a "mock" database (fake database in memory)
- In a real app, this would connect to PostgreSQL, MongoDB, etc.
- Separating database code makes it easy to switch to a real database later!
"""


#
#  Import LIBRARIES
#  Import FILES
from mock dh import MockDatabase, get_database
#

_all_: list[str] = ["MockDatabase", "get_database"]