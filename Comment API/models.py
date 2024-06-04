from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Importance(str, Enum):
    notImportant = "Not Important"
    important = "Important"

class Category(str, Enum):
    fixMe = "Fix Me"
    other = "Other"
    
class Status(str, Enum):
    open = "Open"
    resolved = "Resolved"
    
class Comment(BaseModel):
    commentID: Optional[UUID] = uuid4()
    parentCommentID: Optional[UUID] = None
    childrenCommentIDs: Optional[List[UUID]] = List[None]
    comment: str
    author: str
    datetime: str
    tags: List[str]
    importance: Optional[Importance] = Importance.notImportant
    category: Optional[Category] = Category.other
    status: Optional[Status] = Status.open
    tag: Optional[UUID] = None #context for where the comment is
