import logging

from functools import wraps
import asyncio
from contextlib import contextmanager

from fastapi import HTTPException, status

from src.application.errors import ApplicationRuleError


class FastapiControllerHandler:
    """
    A Decorator Factory to handle service exceptions
    """

    @contextmanager
    def __wrapper(self):
        try:
            yield  # target function execution
        except ApplicationRuleError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message) from exc
        except Exception as exc:
            logging.exception(exc)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            ) from exc

    def __call__(self, func):

        if asyncio.iscoroutinefunction(func):

            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                with self.__wrapper():
                    return await func(*args, **kwargs)

            return async_wrapper
        else:

            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                with self.__wrapper():
                    return func(*args, **kwargs)

            return sync_wrapper
