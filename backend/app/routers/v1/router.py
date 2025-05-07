from typing import Callable

from fastapi import APIRouter

API_PREFIX = "/api/v1"
DEFAULT_TAGS = ["v1"]


def create_factory(prefix: str, tags: list[str], **kwargs) -> Callable[..., APIRouter]:
    def factory(**additional_kwargs) -> APIRouter:
        merged_kwargs = {**kwargs, **additional_kwargs}
        return APIRouter(
            prefix=API_PREFIX + prefix,
            tags=[*tags, *DEFAULT_TAGS],
            **merged_kwargs,
        )

    return factory
