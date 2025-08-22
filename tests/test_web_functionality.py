#!/usr/bin/env python3
"""
Test script to verify web interface functionality.
"""
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_web_imports():
    """Test that all web modules can be imported."""
    try:
        from logus.web import app
        print("✓ Web app imported successfully")
        
        # Test that all routes are defined
        routes = [route.path for route in app.routes]
        expected_routes = ["/", "/agent", "/api/infer-goal", "/api/analyze-fragments", 
                          "/api/analyze-logs", "/api/analyze-prompt", "/api/generate-test", 
                          "/api/execute-prompt"]
        
        for route in expected_routes:
            if route in routes:
                print(f"✓ Route {route} is defined")
            else:
                print(f"✗ Route {route} is missing")
                
        return True
    except ImportError as e:
        print(f"✗ Failed to import web modules: {e}")
        return False
    except Exception as e:
        print(f"✗ Error testing web imports: {e}")
        return False

def test_web_cli_import():
    """Test that the web CLI can be imported."""
    try:
        from logus.web_cli import main
        print("✓ Web CLI imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to import web CLI: {e}")
        return False
    except Exception as e:
        print(f"✗ Error testing web CLI import: {e}")
        return False

if __name__ == "__main__":
    print("Testing web interface functionality...")
    
    success = True
    success &= test_web_imports()
    success &= test_web_cli_import()
    
    if success:
        print("\n✓ All web interface tests passed!")
        sys.exit(0)
    else:
        print("\n✗ Some web interface tests failed!")
        sys.exit(1)