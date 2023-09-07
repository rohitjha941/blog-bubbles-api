from fastapi import APIRouter, HTTPException, Depends, Header
from fastapi import HTTPException, status
from data.models import *
from data import schemas
from auth import helpers as auth_helpers
from auth.models import User
router = APIRouter(
    prefix="/v1",
)

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
        c = await Comments.create(
            position_id=data.identifier_id,
            user_id=user,
            url_id=url['id'],  
            comment=data.comment,
            archor_text=data.anchor_text
        )
        return c.__dict__

    if(data.identifier == None):
        c = await Comments.create(
            user_id=user,
            url_id=url['id'],  
            comment=data.comment,
            archor_text=data.anchor_text
        )
        return c.__dict__
    

    pd = await PositionalData.create(
        identifier=data.identifier,
        url_id=url['id']
    )
    pd = pd.__dict__

    print(pd['id'], user.id, url['id'], data.comment, data.anchor_text)
    c = await Comments.create(
        position_id=pd['id'],
        user_id=user,
        url_id=url['id'],  
        comment=data.comment,
        archor_text=data.anchor_text
    )
    return c.__dict__


@router.get("/comments")
async def comments_get(identifier_id: int = None, url: str = None):
    comments = []
    if(identifier_id != None):
        pd = await PositionalData.get_or_none(id=identifier_id)
        if(pd == None):
            return []
        pd = pd.__dict__
        comments = await Comments.filter(position_id=pd['id']).values()
    elif(url != None):
        url = await Urls.get_or_none(link = url)
        if(url == None):
            return []
        url = url.__dict__
        comments = await Comments.filter(url_id=url['id']).values()
    else:
        raise HTTPException(
            status_code=400,
            detail = [{ "msg" : "Either identifier_id or url is required"}]
        )

    for comment in comments:
        user = await User.get(id=comment['user_id_id'])
        user = user.__dict__
        del user["password"]
        comment['user'] = user
    return comments



@router.delete("/comments/{comment_id}")
async def comments_delete(comment_id: int):
    comment = await Comments.get(id=comment_id)
    await comment.delete()
    return "ok"

@router.get("/identifier")
async def identifier_get(link: str):
    url = await Urls.get_or_none(link = link)
    if  url == None:
        return []
    url = url.__dict__
    pd = await PositionalData.filter(url_id=url['id'])
    return pd
