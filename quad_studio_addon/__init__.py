""" Addon class definition and Settings definition must be imported here.

If addon class or settings definition won't be here their definition won't
be found by QuadPype discovery.
"""
from .addon import QuadStudioAddon, QuadStudioAddonSettingsDef

__all__ = (
    "QuadStudioAddon",
    "QuadStudioAddonSettingsDef"
)
