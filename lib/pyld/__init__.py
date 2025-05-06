""" The PyLD module is used to process JSON-LD. """

from . import jsonld
from .context_resolver import ContextResolver


__version__ = "2.0.5"

__all__ = ["jsonld", "ContextResolver"]
