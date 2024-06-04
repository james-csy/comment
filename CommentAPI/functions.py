from typing import List
from fastapi import HTTPException
from models import Comment
from uuid import UUID

def delete_comment_function(comment_id: UUID, db:List[Comment]):
    #potentially have an authorization step here
    for comment in db:
        if comment.commentID == comment_id:
            #deletes parent comment
            db.remove(comment)
            #deleted nested comments
            children = comment.childrenCommentIDs
            if children is not None:
                for child in children:
                    delete_comment_function(child, db)
            return

    raise HTTPException(
        status_code = 404,
        detail=f"Comment with the id: {comment_id} does not exist."
    )
