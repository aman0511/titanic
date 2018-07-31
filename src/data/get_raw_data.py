
import os
from dotenv import load_dotenv, find_dotenv
from requests import session
import logging

payload = {
    'action':"login",
    "username": os.environ.get("KAGGLE_USERNAME"),
    "password": os.environ.get("KAGGLE_PASSWORD")
}

url = "https://www.kaggle.com/c/titanic/download/train.csv"

def extract_data(url, file_path):
    with session() as c:
        c.post("https://www.kaggle.com/accounts/login/", data=payload)
        response = c.get(url)
        for block in response.iter_content(1024):
            handle.write(block)

def main(project_dir):
    
    logger = logging.getLogger(__name__)
    
    logger.info("getting raw data")
    
    train_url = "https://www.kaggle.com/c/titanic/download/train.csv"
    test_url = "https://www.kaggle.com/c/titanic/download/test.csv"
    
    
    raw_data_path  = os.path.join(project_dir, "data", "raw")
    train_data_path = os.path.join(raw_data_path, "train_data.csv")
    test_data_path = os.path.join(raw_data_path, "test_data.csv")
    
    logger.info("downloaded raw training data and test data")

    
    extract_data(train_url, train_data_path)
    extract_data(test_url, test_data_path)


if __name__ == "__main__":
    
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    main(project_dir)