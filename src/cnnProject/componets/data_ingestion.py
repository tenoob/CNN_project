#DataIngestionComponent
import os
import urllib.request as request
from zipfile import ZipFile
from cnnProject.entity import DataIngestionConfig
from cnnProject import logger
from cnnProject.utils import get_size
from tqdm import tqdm
from pathlib import Path

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config = config

    def download_file(self):
        logger.info(f"Trying to Download file.....")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Started Download...")
            filename , headers = request.urlretrieve(
                url=self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"filename:{filename} downloaded with following information:\n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    #hidden method to check and take only jpg imgs
    def _get_updated_list_of_files(self,list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self,zf:ZipFile,f:str , working_dir:str):
        target_file_path = os.path.join(working_dir,f)
        if  not os.path.exists(target_file_path):
            zf.extract(f,working_dir)

        if os.path.getsize(target_file_path) == 0:
            logger.info(f"Removing file:{target_file_path} with size: {get_size(Path(target_file_path))}")
            os.remove(target_file_path)

    def unzip_and_clean(self):
        logger.info(f"Unzipping file and removing unwanted files")
        with ZipFile(file=self.config.local_data_file,mode='r') as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files=list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf,f,self.config.unzip_dir)
