"""craterpy module"""
from craterpy.dataset import CraterpyDataset
from craterpy.roi import CraterRoi

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version(__package__)
