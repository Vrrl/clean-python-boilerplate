from typing import List, Optional

from supertokens_python.recipe.emailpassword.asyncio import get_user_by_id
from supertokens_python.recipe.userroles.asyncio import get_roles_for_user

# from sqlalchemy.orm.exc import NoResultFound

from src.application.interfaces.repository.user import (
    FindUserByIdRepositoryInterface,
    ListUserRolesByIdRepositoryInterface,
)


class UserRepository(FindUserByIdRepositoryInterface, ListUserRolesByIdRepositoryInterface):
    """Class to manage supertokens repository of users"""

    async def find_by_id(self, id: str):
        """Find data by id in Repository"""

        user = await get_user_by_id(id)
        return user

    async def list_user_roles_by_id(self, id: str) -> list:
        """Find roles data by id in Repository"""

        roles = (await get_roles_for_user(id)).roles
        return roles
