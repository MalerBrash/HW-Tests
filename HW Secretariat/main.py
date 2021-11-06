import pytest
from unittest.mock import patch
from app import *

# 'p' get_doc_owner_name() print('Владелец документа - {}'.format(owner_name))
# 'ap' uniq_users = get_all_doc_owners_names() print('Список владельцев документов - {}'.format(uniq_users))
# 'l' show_all_docs_info()
# 's' directory_number = get_doc_shelf() print('Документ находится на полке номер {}'.format(directory_number))
# 'a' new_doc_shelf_number = add_new_doc() print('\nНа полку "{}" добавлен новый документ:'.format(new_doc_shelf_number))
# 'd' doc_number, deleted = delete_doc()    if deleted: print('Документ с номером "{}" был успешно удален'.format(doc_number))
# 'm' move_doc_to_shelf()
# 'as' shelf_number, added = add_new_shelf() if added: print('Добавлена полка "{}"'.format(shelf_number))


class TestPytest:

    def setup(self):
        print('Старт тестирования')

    @patch('builtins.input', return_value='2207 876234')
    def test_get_doc_owner_name(self, mock_input):
        assert get_doc_owner_name() == 'Василий Пупкин'

    def test_get_all_doc_owners_names(self):
        assert get_all_doc_owners_names() == {'Геннадий Покемонов', 'Василий Пупкин', 'Аристарх Павлов'}

    @patch('builtins.input', return_value='11-2')
    def test_get_doc_shelf(self, mock_input):
        assert get_doc_shelf() == '1'

    @patch('builtins.input', side_effect=['0310 555555', 'passport', 'Василий Алиба', '4'])
    def test_add_new_doc(self, mock_input):
        assert add_new_doc() == '4'

    @patch('builtins.input', return_value='11-2')
    def test_delete_doc(self, mock_input):
        assert delete_doc() == ('11-2', True)

    @patch('builtins.input', side_effect=['2207 876234', '4'])
    def test_move_doc_to_shelf(self, mock_input):
        assert move_doc_to_shelf() == 'Документ номер "2207 876234" был перемещен на полку номер "4"'

    @patch('builtins.input', return_value='5')
    def test_add_new_shelf(self, mock_input):
        assert add_new_shelf() == ('5', True)

    def test_show_all_docs_info(self):
        assert show_all_docs_info() == [
                'passport "2207 876234" "Василий Пупкин"',
                'insurance "10006" "Аристарх Павлов"',
                'passport "0310 555555" "Василий Алиба"']

    def teardown(self):
        print('Тест завершен')


if __name__ == '__main__':
    pytest.main()
