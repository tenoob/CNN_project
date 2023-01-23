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


#what dvc does?
it has stages(stages) and in each stage there are commands(cmd) and dependencies(deps) which generate some output(outs) 

during first use do *dvc init* to iitialize dvc
then it will creage a .dvcignore and .dvcyaml 

for next time execution - dvc repro

dvc dag ->cmd to view how the stages and deps are connected