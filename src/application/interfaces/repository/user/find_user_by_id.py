from abc import ABC, abstractmethod

from src.domain.models import Process


class FindUserByIdRepositoryInterface(ABC):
    """Interface to Repository"""

    # pylint: disable=redefined-builtin
    @abstractmethod
    async def find_by_id(self, id: str) -> Process:
        """abstractmethod"""

        raise NotImplementedError()
