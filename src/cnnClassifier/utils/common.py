from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import os

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded sucessfukky")
            logger.info(f"content {content}")
            return ConfigBox(content)
    except BoxValueError:
        logger(f"path_to_yaml {path_to_yaml}")
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

def create_directorries(path_to_directories:list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"create dire ctory at :{path}")

@ensure_annotations
def get_size(path: Path)->str:
    """get size KB,arg path of file
    return size in KB"""
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb}"

# def save_bin


     
# print("f")
# b = read_yaml(Path("D:\Arambh\project\kedney\Kidney-Disease-Classification\config\config.yaml"))
# print(b)
# # print(get_size(Path("D:\Arambh\project\kedney\Kidney-Disease-Classification\config\config.yaml")))