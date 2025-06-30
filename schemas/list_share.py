from enum import Enum


class RoleEnum(str, Enum):
    owner = "owner"
    editor = "editor"
    viewer = "viewer"
