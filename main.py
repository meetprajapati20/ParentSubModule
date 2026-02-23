from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Zetta API & Frontend")

# ==========================================
# 1. ADD ALL YOUR API ROUTERS FIRST
# ==========================================
try:
    from server_module1.routers.module1 import router as m1_router
    app.include_router(m1_router, prefix="/api/module1")
except ImportError:
    pass

# ... add other API modules ...


# ==========================================
# 2. SERVE THE REACT FRONTEND (PRODUCTION ONLY)
# ==========================================

# Define the path where the React build folder will live inside the server
FRONTEND_BUILD_DIR = os.path.join(os.path.dirname(__file__), "..", "client-shell", "build")

# Check if the build folder exists (it won't during local dev, only in prod)
if os.path.exists(FRONTEND_BUILD_DIR):
    
    # Serve the static JS/CSS assets. 
    # Based on your package.json, React expects them at /zetta/static
    static_path = os.path.join(FRONTEND_BUILD_DIR, "static")
    if os.path.exists(static_path):
        app.mount("/static", StaticFiles(directory=static_path), name="static")

    # Catch-all route for React Router (SPA Fallback)
    # This MUST be at the very bottom of the file!
    @app.get("/{full_path:path}")
    async def serve_react_app(full_path: str):
        # If the user requests a specific file (like favicon.ico or a manifest), serve it
        requested_file = os.path.join(FRONTEND_BUILD_DIR, full_path)
        if os.path.isfile(requested_file):
            return FileResponse(requested_file)
        
        # Otherwise, return the main React index.html and let React Router handle the URL
        return FileResponse(os.path.join(FRONTEND_BUILD_DIR, "index.html"))

else:
    print("⚠️ Frontend build folder not found. Serving API only (Local Dev Mode).")