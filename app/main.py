from fastapi import FastAPI

from app.api.routers import general, items, models, users

app = FastAPI()

app.include_router(general.router)
app.include_router(items.router)
app.include_router(users.router)
app.include_router(models.router)
