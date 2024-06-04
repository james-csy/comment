from typing import List
from fastapi import FastAPI
from models import Comment, Importance, Category, Status
from uuid import UUID, uuid4

app = FastAPI()

#Temporary Dummy Database
db: List[Comment] = [
    Comment(
        commentID=uuid4(),
        parentCommentID=None,
        childrenCommentIDs=None,
        comment="This is a test comment",
        author="james.chong@aetna.com",
        datetime="June 6th 2024",
        tags=["jason.chong@aetna.com", "jameschong@berkeley.edu"],
        importance=Importance.notImportant,
        category=Category.fixMe,
        status=Status.open,
        context=uuid4() #replace with context id in the future
    )
]

@app.get("/api/v1/comments")
def fetch_comments():
    return db