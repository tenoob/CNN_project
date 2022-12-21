import pytest
from cnnProject.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError


class Test_read_yaml:
    yaml_files = ["tests/data/empty.yaml", "tests/data/demo.yaml"]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_files[0]))

    def test_read_yaml_return_type(self):
        response = read_yaml(Path(self.yaml_files[1]))
        assert isinstance(response, ConfigBox)
        # assert checks the condition written in front of them is True or not
        # if False then shows assert is not correct

    # @pytest.mark.parametrize() make sure that insted of passing 1 file at a time
    # we can pass a list of files(yaml_files) as Path_to_yaml
    @pytest.mark.parametrize("path_to_yaml", yaml_files)
    def test_read_yaml_bad_data_type(self, path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)
