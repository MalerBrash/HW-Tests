import pytest
from app import *


class TestPyTest:
    def setup(self):
        print('Start testing')

    @pytest.mark.parametrize('folder_name, expected_res', [('Test_folder', 404)])
    def test_get_status_folder(self, folder_name, expected_res):
        assert get_status_folder(folder_name) == expected_res

    @pytest.mark.parametrize('folder_name, expected_res', [('Test_folder', 201), ('Test_folder', 409)])
    def test_create_new_folder(self, folder_name, expected_res):
        assert create_new_folder(folder_name) == expected_res

    @pytest.mark.parametrize('folder_name, expected_res', [('Test_folder', 201)])
    def test_get_status_folder(self, folder_name, expected_res):
        assert get_status_folder(folder_name) == expected_res

    @pytest.mark.parametrize('folder_name, expected_res', [('Test_folder', 204), ('Test_folder1', 404)])
    def test_delete_folder(self, folder_name, expected_res):
        assert delete_folder(folder_name) == expected_res

    @pytest.mark.parametrize('folder_name, expected_res', [('Test_folder', 404)])
    def test_get_status_folder(self, folder_name, expected_res):
        assert get_status_folder(folder_name) == expected_res

    def teardown(self):
        print('testing completed')


if __name__ == '__main__':
    pytest.main()
