from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_company_name():
    return {"company_name": "example 1"}

@router.get("/employees")
async def number_of_users():
    return 144