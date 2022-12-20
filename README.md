#CNN project
python 3.7
dlenv
commands 
    - for settingup test env (bash init_setup.sh)
    - to run pytest (pytest -v)
    - to run tox.ini (tox)
    - to rerun tox if new packages are added to requirements (tox --recreate)


##workflow

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