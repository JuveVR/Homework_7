from Homework_6.Exercise_1 import book_dict, base_url_book, add_new_item, add_item_id, check_item_in_list, \
    compare_dicts, check_new_item, book_update_and_check, delete_item_finally
import unittest
import uuid
import random
import re



class TestAddNewBook(unittest.TestCase):
    def setUp(self):

        self.book_dict = book_dict

    def tearDown(self):
        delete_item_finally(base_url_book, self.book_id)

    def test_new_book_id_type(self):
        self.book_id = add_new_item(base_url_book, book_dict)
        self.assertEqual(type(self.book_id), str)

    def test_new_book_id_emptiness(self):
        self.book_id = add_new_item(base_url_book, book_dict)
        self.assertTrue(self.book_id)



class AddNewBookNegative(unittest.TestCase):
    def setUp(self):
        self.base_url = base_url_book

    def test_creation_without_title(self):
        with self.assertRaises(Exception) as ex:
            wrong_book = {"title": None, "author": "Myauthor"}
            add_new_item(base_url_book, wrong_book)
        self.assertEqual("Item hasn't been added", str(ex.exception))

    def test_creation_without_author(self):
        with self.assertRaises(Exception) as ex:
            wrong_book = {"title": "Mytitle", "author": None}
            add_new_item(base_url_book, wrong_book)
        self.assertEqual("Item hasn't been added", str(ex.exception))


class TestAddItemIdFunc(unittest.TestCase):
    def test_correct_addition(self):
        book = {"title": "Mytitle", "author": "My_author"}
        add_item_id(book, 22)
        self.assertEqual(book["id"], 22)

    def test_correct_id_update(self):
        book = {"title": "Mytitle", "author": "My_author", "id": 100}
        add_item_id(book, 1)
        self.assertEqual(book["id"], 1)


class TestDictCompareFunc(unittest.TestCase):
    def setUp(self):
        self.dict1 = {"title": "Mytitle", "author": "My_author", "id": 100}
        self.dict2 = {"title": "Mytitle", "author": "My_author", "id": 100}
        self.dict3 = {"title": "Mytitle", "author": "My_author", "id": 20200}

    def test_compare_equal(self):
        result = compare_dicts(self.dict1, self.dict2)
        self.assertIsNone(result)

    def test_compare_not_equal(self):
        with self.assertRaises(Exception) as ex:
            compare_dicts(self.dict2, self.dict3)
        self.assertEqual("Dicts are not equal", str(ex.exception))


class TestCheckNewItemBook(unittest.TestCase):
    def setUp(self):
        self.base_url = base_url_book
        self.book_dict = book_dict
        self.book_id = add_new_item(base_url_book, book_dict)

    def tearDown(self):
        delete_item_finally(base_url_book, self.book_id)

    def test_check_correct_data(self):
        result = check_new_item(base_url_book, self.book_id, book_dict)
        self.assertIsNone(result)

    def test_check_with_wrong_id(self):
        with self.assertRaises(Exception) as ex:
            check_new_item(base_url_book, str(random.randint(4000000000, 9120000001)), book_dict)
        self.assertEqual("Wrong request", str(ex.exception))

    def test_book_in_list(self):
        result = check_item_in_list(base_url_book, self.book_id, book_dict)
        self.assertIsNone(result)

    def test_book_in_list_wrong_id(self):
        with self.assertRaises(Exception) as ex:
            check_item_in_list(base_url_book, str(random.randint(4000000000, 9120000001)), book_dict)
        self.assertEqual("The item is not in the list", str(ex.exception))


class TestBookUpdate(unittest.TestCase):
    def setUp(self):
        self.base_url = base_url_book
        self.book_dict = book_dict
        self.book_id = add_new_item(base_url_book, book_dict)

    def tearDown(self):
        delete_item_finally(base_url_book, self.book_id)

    def test_updated_data(self):
        result = book_update_and_check(base_url_book, self.book_id, book_dict, new_title=str(uuid.uuid4()),
                                       new_author=str(uuid.uuid4()))
        self.assertIsNone(result)

    def test_update_one_parameter(self):
        result = book_update_and_check(base_url_book, self.book_id, book_dict, new_title=str(uuid.uuid4()))
        self.assertIsNone(result)

    def test_update_attempt_wrong_id(self):
        with self.assertRaises(Exception) as ex:
            book_update_and_check(base_url_book, str(random.randint(4000000000, 9120000001)), book_dict,
                                           new_title=str(uuid.uuid4()), new_author=str(uuid.uuid4()))
        self.assertEqual("Wrong request", str(ex.exception))

    def test_attempt_update_wrong_url(self):
        with self.assertRaises(Exception) as ex:
            book_update_and_check(base_url_book+"wrong", str(random.randint(4000000000, 9120000001)), book_dict,
                                           new_title=str(uuid.uuid4()), new_author=str(uuid.uuid4()))
        self.assertEqual("Wrong request", str(ex.exception))




class TestDeleteItemFunc(unittest.TestCase):
    def setUp(self):
        self.base_url = base_url_book
        self.book_dict = book_dict
        self.book_id = add_new_item(base_url_book, book_dict)

    def tearDown(self):
        delete_item_finally(base_url_book, self.book_id)

    def test_delete_existent(self):
        new_test_id = add_new_item(base_url_book, book_dict)
        result = delete_item_finally(base_url_book, new_test_id)
        self.assertIsNone(result)

    def test_try_delete_with_id_none(self):
        with self.assertRaises(Exception) as ex:
            delete_item_finally(base_url_book, None)
        self.assertEqual("Item id is None", str(ex.exception))

    def test_try_delete_with_wrong_id(self):
        with self.assertRaises(Exception) as ex:
            delete_item_finally(base_url_book, str(random.randint(4000000000, 9120000001)))
        self.assertEqual("Wrong request status code. Item hasn't been deleted", str(ex.exception))



if __name__ == '__main__':
    from HtmlTestRunner import HTMLTestRunner
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"C:\Users\user\workspace_python\Homeworks\Test_unit_test_Homework_7"))

    testCreate1 = TestAddNewBook("test_new_book_id_type")
    testCreate2 = TestAddNewBook("test_new_book_id_emptiness")
    testDelete = TestDeleteItemFunc("test_delete_existent")
    smoke_suite = unittest.TestSuite([testCreate1, testCreate2, testDelete])
    result = unittest.TestResult()
    smoke_suite.run(result)
    print(result)
































