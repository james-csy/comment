from typing import List
from fastapi import FastAPI
from models import Comment, Importance, Category, Status
from uuid import UUID, uuid4

app = FastAPI()

#Temporary Dummy Database
db: List[Comment] = [
    Comment(
        commentID="ac598b80-a96e-4848-b292-d84bcc8554e1",
        parentCommentID=None,
        childrenCommentIDs=["34c8117f-2700-43db-8568-71151c8ac5c4"], #check if this List format is valid
        comment="This is a test comment",
        author="james.chong@aetna.com",
        datetime="June 6th 2024",
        tags=["jason.chong@aetna.com", "jameschong@berkeley.edu"],
        importance=Importance.notImportant,
        category=Category.fixMe,
        status=Status.open,
        context=uuid4() #replace with context id in the future
    ),
    Comment(
        commentID="34c8117f-2700-43db-8568-71151c8ac5c4",
        parentCommentID="ac598b80-a96e-4848-b292-d84bcc8554e1",
        childrenCommentIDs=None,
        comment="This is also a test comment",
        author="james.chong@aetna.com",
        datetime="June 7th 2024",
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