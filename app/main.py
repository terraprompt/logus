"""
Backward compatibility entry point for Blogus.
"""

from blogus.web import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
