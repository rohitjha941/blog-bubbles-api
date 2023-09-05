from fastapi import APIRouter, HTTPException, Depends, Header
from fastapi import HTTPException, status
from data.models import *
from data import schemas
from auth import helpers as auth_helpers

router = APIRouter(
    prefix="/data",
)

# @router.post("/url")
# async def url_post(data: schemas.UrlsSchema):
#     url = await Urls.create(
#         link=data.url
#     )
#     return url.__dict__

# @router.get("/url")
# async def url_get():
#     url = await Urls.all()
#     return url

# @router.get("/url/{id}")
# async def url_get(id: int):
#     url = await Urls.get(id=id)
#     return url


@router.post("/comments")
async def comments_post(data: schemas.PositionalDataWithCommentsSchema, user=Depends(auth_helpers.validateToken)):
    try:
        url = await Urls.get(link = data.url)
        url = url.__dict__
    except:
        url = await Urls.create(
            link=data.url
        )
        url = url.__dict__

    c = await Comments.create(
        user_id=user.id,
        url_id=url['id'],  
        comment=data.comment,
        identifier=data.identifier
    )
    return "ok"


@router.get("/comments/{url_id}")
async def comments_get(url_id: int):
    comments = await Comments.filter(url_id=url_id)
    return comments


@router.delete("/comments/{comment_id}")
async def comments_delete(comment_id: int):
    comment = await Comments.get(id=comment_id)
    await comment.delete()
    return "ok"
