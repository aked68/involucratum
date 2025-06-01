from typing import Callable

from deepmerge import Merger
from fastapi import APIRouter

API_PREFIX = "/api/v1"
DEFAULT_TAGS = ["v1"]

# マージャーの設定
merger = Merger(
    [(dict, "merge")],  # 辞書型はマージ
    ["override"],  # その他は上書き
    ["override"],
)


def create_factory(prefix: str, tags: list[str], **kwargs) -> Callable[..., APIRouter]:
    def factory(**additional_kwargs) -> APIRouter:
        # merged_kwargs = kwargs.copy()
        # for key, value in additional_kwargs.items():
        #     if (
        #         key in merged_kwargs
        #         and isinstance(merged_kwargs[key], dict)
        #         and isinstance(value, dict)
        #     ):
        #         merged_kwargs[key] = {**merged_kwargs[key], **value}
        #     else:
        #         merged_kwargs[key] = value

        merged_kwargs = merger.merge(kwargs.copy(), additional_kwargs)

        return APIRouter(
            prefix=API_PREFIX + prefix,
            tags=[*tags, *DEFAULT_TAGS],
            **merged_kwargs,
        )

    return factory
