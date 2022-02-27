from . import models
from .config import Settings
from .database import engine
from .routers import auth, posts, users, vote
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# sqlalchemy before alembic:
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello world!! Pushing out to ubuntu"}


#####DATABASE CONNECTION#####



# #####FAKE DATABASE#####
# my_posts = [
#     {"title": "title of post 1", "content": "content of post 1", "id": 1}, 
#     {"title": "favorite foods", "content": "I like pizza", "id": 2},
# ]


#####FUNCTIONS#####
# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i




