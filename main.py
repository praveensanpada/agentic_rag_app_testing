# === main.py ===
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.mongo_routes import router as mongo_router
import uvicorn
from config.settings import PORT

app = FastAPI(title="Cric DataHub Mongo API")

app.include_router(mongo_router, prefix="/mongo", tags=["Mongo"])

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Cric DataHub Status</title>
        </head>
        <body style='font-family:Arial, sans-serif;'>
            <h1>🏏 Cric DataHub is running!</h1>
            <p>Server URL: <code>http://0.0.0.0:8088/</code></p>
            <h3>Available Endpoints:</h3>
            <ul>
                <li><strong>GET</strong> <code>/mongo/get_venue_detail?venue_uid=51</code></li>
                <li><strong>POST</strong> <code>/mongo/add_venue</code> — Add new venue</li>
            </ul>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)