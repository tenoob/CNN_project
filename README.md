# CNN project
python 3.7
10sept
commands 
    - for settingup test env (bash init_setup.sh)
    - to run pytest (pytest -v)
    - to run tox.ini (tox)
    - to rerun tox if new packages are added to requirements (tox --recreate)


## workflow

1.  Update config.yaml -> Configrationfile
2.  Update secrets.yaml (not used in this project)
3.  Update params.yaml
4.  Update entity
5.  Update configuration manager in src config
6.  Update the compoents
7.  Update the pipeline
8.  Test run pipeline
9.  run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline

# DVC (Data Version Control)

what dvc does?
it has stages(stages) and in each stage there are commands(cmd) and dependencies(deps) which generate some output(outs) 

*DVC is built to assist mlops in handling large files, data sets, machine learning models, and metrics. It is commonly used to make machine learning experiments reproducible*


during first use do *dvc init* to iitialize dvc
then it will creage a .dvcignore and .dvcyaml 

for next time execution - dvc repro

dvc dag ->cmd to view how the stages and deps are connected

params in dvc are taken from entity for each dataclass

# DagsHub

DAGsHub is similar to GitHub which assists data scientists and machine learning engineers in sharing the data, models, experiments, and code. It allows you and your team to easily share, review, and reuse your work, providing a GitHub experience for machine learning.

*it comes with experiments, mlflow integration, machine learning pipeline visualization, performance metrics comparison, and visualizations.*

# MLflow

to see the ui -> mlflow ui
or we can run the mlflow server which will run all the training in db instead of file based system

cmd (try running in bash unable to run in cmd for me)

mlflow server \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./artifacts \
--host 127.0.0.1 -p 1234

or can use dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/tenoob/CNN_project.mlflow \
MLFLOW_TRACKING_USERNAME=tenoob \
MLFLOW_TRACKING_PASSWORD=<> \
python script.py

# Streamlit

Used for creating an UI and deploying the model there 
to run streamlit app -> streamlit run app.py


# DOcker
cmd to create an image -> docker build -t name .
cmd to rum an image -> docker run -p 8501:8501 container_name  

<br>
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
