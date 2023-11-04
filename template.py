import os
import logging
from pathlib import Path



logging.basicConfig(format= ("%(levelname)s - %(message)s"),level=logging.INFO)

project_name = "MLproject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "Dockerfile",
    "app.py",
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)


    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"{file_dir} is created for {filename}")


    if (not os.path.exists(filepath))  or (os.path.getsize(filepath) ==0) :
        with open(filepath,"w") as filepath_obj:
            pass
        logging.info(f"{filepath} is created")


    else:
        logging.info(f"{filepath} is already existed")