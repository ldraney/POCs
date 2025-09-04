#!/usr/bin/env python
"""
Development server runner for Namespace Service
"""

import uvicorn
from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD or True,
        log_level="info"
    )