from cnnProject import logger
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import yaml,json,joblib,os


@ensure_annotations
def read_yaml(file_path:Path) -> ConfigBox:
    """
    read yaml file and returns

    Args:
        file_path (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(file_path) as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

    @ensure_annotations
    def save_json(path:Path , data: dict):
        """
        Save json data

        Args:
            path(Path): path to json file
            data(dict): data to be saved in json file
        """ 
        with open(path,"w") as f:
            json.dump(data,f,indent=4)

        logger.info(f"json file saved at: {path}")

    
    @ensure_annotations
    def load_json(path:Path) -> ConfigBox:
        """
        load json files data

        Args:
            path(Path): path to json file
        
        Return:
            ConfigBox: data as class arrtibutes instead of dict
        """
        with open(path) as f:
            content = json.load(f)

        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)


    @ensure_annotations
    def save_bin(data:Any , path:Path):
        """
        save binary file

        Args:
            data(Any): data to be saved as binary
            path(Path): path to binary file
        """
        joblib.dump(value=data,filename=path)
        logger.info(f"binary file saved at: {path}")

    
    @ensure_annotations
    def load_bin(path:Path) -> Any:
        """
        load binary data

        Args:
            path(Path): path to binary file

        Returns:
            Any: object stored in the file
        """
        data = joblib.load(data)
        logger.info(f"binary file loaded from: {path}")
        return data

    @ensure_annotations
    def get_size(path:Path) -> str:
        """
        get size in KB

        Args:
            path(Path): path of the file

        Returns:
            str: size in KB
        """
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"

