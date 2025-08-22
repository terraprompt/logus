"""
Backward compatibility entry point for Logus.
"""

from logus.web import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
