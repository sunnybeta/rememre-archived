from fastapi import APIRouter


router = APIRouter()

from . import user, auth

router.include_router(user.router)
router.include_router(auth.router)
