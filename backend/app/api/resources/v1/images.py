from fastapi import APIRouter
from fastapi.responses import StreamingResponse


router = APIRouter()


@router.get('/show/{file_name}')
async def get_images(file_name: str):
    def iterfile():  
        with open('./api/resources/v1/tmp/'+file_name, mode="rb") as file_like:  
            yield from file_like  
    return StreamingResponse(iterfile(), media_type="image/png")