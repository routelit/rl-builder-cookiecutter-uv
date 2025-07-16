from typing import ClassVar, Optional

from routelit import AssetTarget, RouteLitBuilder  # type: ignore[import-untyped]


class RLBuilder(RouteLitBuilder):  # type: ignore[no-any-unimported]
    """
    A builder for a RouteLit application.
    This Builder template serves as example on how to create a RouteLit custom components.
    """

    static_assets_targets: ClassVar[list[AssetTarget]] = [  # type: ignore[no-any-unimported]
        {
            "package_name": "{{cookiecutter.project_slug}}",
            "path": "static",
        }
    ]

    def hello(self, name: str, key: Optional[str] = None) -> None:
        self._create_element(name="hello", props={"name": name}, key=key or self._new_text_id("hello"))

    def hello_world(self) -> None:
        self.hello("world")
