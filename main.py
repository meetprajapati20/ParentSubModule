from fastapi import FastAPI
app = FastAPI(title="Zetta API Shell")

# 1. Load Shared Utils
try:
    from ServerModule1.server.utils.helpers import get_version
    print(f"Loaded Shared Utils v{get_version()}")
except ImportError:
    pass

# 2. Dynamically Load Modules
try:
    from ServerModule2.routers.module1 import router as m1_router
    app.include_router(m1_router, prefix="/api/module1")
    print("✅ Module 1 loaded")
except ImportError:
    print("⚠️ Module 1 not found locally. Skipping.")