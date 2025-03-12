from fastapi import APIRouter

router = APIRouter()


@router.get("/foo")
async def foo():
    print("foo called")
    return {"message": "foo"}
