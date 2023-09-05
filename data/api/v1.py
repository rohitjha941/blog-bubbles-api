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

    if(data.identifier_id != None):
        comment = await Comments.create(
            position_id=data.identifier_id,
            user_id=user.id,
            url_id=url['id'],  
            comment=data.comment,
            anchor_text=data.anchor_text
        )
        return "ok"

    # print(data.identifier_id)

    pd = await PositionalData.create(
        identifier=data.identifier,
        url_id=url['id']
    )
    pd = pd.__dict__

    c = await Comments.create(
        position_id=pd['id'],
        user_id=user.id,
        url_id=url['id'],  
        comment=data.comment,
        archor_text=data.anchor_text
    )
    return "ok"


@router.get("/comments/{identifier_id}")
async def comments_get(identifier_id: int):
    pd = await PositionalData.get(id=identifier_id)
    pd = pd.__dict__
    comments = await Comments.filter(position_id=pd['id'])
    return comments


@router.delete("/comments/{comment_id}")
async def comments_delete(comment_id: int):
    comment = await Comments.get(id=comment_id)
    await comment.delete()
    return "ok"

@router.get("/identifier")
async def identifier_get(url: str):
    url = await Urls.get(link = url)
    url = url.__dict__
    pd = await PositionalData.filter(url_id=url['id'])
    return pd

@router.get("/comments_by_url")
async def comments_by_url_get(schema: schemas.UrlsSchema):
    url = await Urls.get(link = schema.link)
    url = url.__dict__
    comments = await Comments.filter(url_id=url['id'])
    return comments