import logging

from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer

from fastapi import APIRouter, Depends, HTTPException, status

from src.main.adapter import FastapiControllerHandler

router = APIRouter(tags=["users"], prefix="/v1/users")

### User


@router.get("/{id}")
@FastapiControllerHandler()
def detail_user(
    id: str,
    session: SessionContainer = Depends(verify_session()),
):
    """Detail user information"""
    # TODO: use case flow
    raise NotImplementedError()
