from pydantic import BaseModel

# Schema/Pydantic model -> define structure of a request & response
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass
