# from src.cnnClassifier import logger

# logger.info("wellcome to our custom log")

from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotation
from box import ConfigBox
from pathlib immport Path
from typing import Any
import base64

@def read_yaml(path_to_yaml:Path)->ConfigBox:
