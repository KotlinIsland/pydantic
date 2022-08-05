from pydantic.dataclasses import dataclass


@dataclass
class Foo:
    ...


@dataclass(config={})
class Bar:
    ...
