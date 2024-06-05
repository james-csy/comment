from typing import List
from fastapi import FastAPI, HTTPException
from models import Comment, Importance, Category, Status, CommentUpdates
from functions import delete_comment_function
from uuid import UUID, uuid4

app = FastAPI()

#Temporary Dummy Database
db: List[Comment] = [
    Comment(
        commentID="ac598b80-a96e-4848-b292-d84bcc8554e1",
        parentCommentID=None,
        childrenCommentIDs=["34c8117f-2700-43db-8568-71151c8ac5c4"],
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


@app.post("/api/v1/comments")
def add_comment(comment: Comment):
    #comment infomration should be in the body of Post Request
    db.append(comment)
    return comment

@app.delete("/api/v1/comments/{comment_id}")
def delete_comment(comment_id: UUID):
    #potentially have an authorization step here
    delete_comment_function(comment_id, db)
    #function used to avoid recursively calling the API
    return db

@app.put("/api/v1/comments/{comment_id}")
def update_comment(comment_id:UUID, comment_updates: CommentUpdates):
    #potentially have an authorization step here
    for comment in db:
        if comment_updates.importance is not None:
            comment.importance = comment_updates.importance
        if comment_updates.category is not None:
            comment.category = comment_updates.importance
        if comment_updates.status is not None:
            comment.status = comment_updates.status
        return
    raise HTTPException(
        status_code = 404,
        detail=f"Comment with the id: {comment_id} does not exist."
    )

