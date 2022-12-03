from abc import ABC, abstractmethod

from src.domain.models import Process


class ListUserRolesByIdRepositoryInterface(ABC):
    """Interface to Repository"""

    # pylint: disable=redefined-builtin
    @abstractmethod
    async def list_user_roles_by_id(self, id: str) -> Process:
        """abstractmethod"""

        raise NotImplementedError()
