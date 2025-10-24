"""
🛣️ Routers Package

This folder contains all our API routes (endpoints).
Getting Started:
- Routes are like different pages on a website
- Each route handles a specific type of request (GET, POST, etc.)
- Separating routes makes the code easier to understand and maintain
"""

#
#  Import LIBRARIES
#  Import FILES
from .general import router as general_router
from .students import router as students_router
from .subjects import router as subjects_router

#


__all__ = ["students_router", "subjects_router", "general_router"]
