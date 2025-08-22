"""
Tests for the web interface of Blogus.
"""

import pytest


def test_web_import():
    """Test that the web module can be imported without errors."""
    try:
        from blogus import web

        assert web is not None
    except ImportError as e:
        # This is expected if web dependencies are not installed
        # We just want to make sure it doesn't crash unexpectedly
        assert "fastapi" in str(e) or "uvicorn" in str(e)
