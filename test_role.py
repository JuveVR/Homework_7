from Homework_6.Exercise_1 import book_dict, role_dict, base_url_book, base_url_role, add_new_item, add_item_id, check_item_in_list, \
    compare_dicts, check_new_item, role_update_and_check, delete_item_finally
import unittest
import uuid
import random



class TestAddNewRole(unittest.TestCase):
    def setUp(self):
        self.book_id = add_new_item(base_url_book, book_dict)
        self.role_dict = role_dict
        role_dict["book"] = "{}{}".format(base_url_book, self.book_id)

    def tearDown(self):
        delete_item_finally(base_url_role, self.role_id)
        delete_item_finally(base_url_book, self.book_id)

    def test_new_role_id_type(self):
        self.role_id = add_new_item(base_url_role, role_dict)
        self.assertEqual(type(self.role_id), str)

    def test_new_role_id_emptiness(self):
        self.role_id = add_new_item(base_url_role, role_dict)
        self.assertTrue(self.role_id)

    def test_creation_without_level(self):
        wrong_role = {"name": "Mtsiri",
                      "type": "classic",
                      "book": "{}{}".format(base_url_book, self.book_id),
                      "level": None
                      }
        self.role_id = add_new_item(base_url_role, wrong_role)
        self.assertEqual(type(self.role_id), str)

    def test_creation_without_book(self):
        wrong_role = {"name": "Mtsiri",
                      "type": "classic",
                      "book": None,
                      "level": 122
                      }
        self.role_id = add_new_item(base_url_role, wrong_role)
        self.assertTrue(self.role_id)


class AddNewRoleExept(unittest.TestCase):
    def setUp(self):
        # self.base_url = base_url_role
        self.book_id = add_new_item(base_url_book, book_dict)
        self.role_dict = role_dict

    def tearDown(self):
        # delete_item_finally(base_url_role, self.role_id)
        delete_item_finally(base_url_book, self.book_id)

    def test_creation_without_name(self):
        with self.assertRaises(Exception) as ex:
             wrong_role = {"name": None,
                           "type":"detective",
                           "book": "{}{}".format(base_url_book, self.book_id),
                           "level": 100500
                          }
             add_new_item(base_url_role, wrong_role)

        self.assertEqual("Item hasn't been added", str(ex.exception))

    def test_creation_without_type(self):
        with self.assertRaises(Exception) as ex:
            wrong_role = {"name": "Mtsiri",
                          "type": None,
                          "book": "{}{}".format(base_url_book, self.book_id),
                          "level": 100500
                          }
            add_new_item(base_url_role, wrong_role)
        self.assertEqual("Item hasn't been added", str(ex.exception))

    def test_creation_with_str_level(self):
        with self.assertRaises(Exception) as ex:
            wrong_role = {"name": "Mtsiri",
                          "type": "classic",
                          "book": "{}{}".format(base_url_book, self.book_id),
                          "level": "level"
                          }
            add_new_item(base_url_role, wrong_role)
        self.assertEqual("Item hasn't been added", str(ex.exception))

    def test_creation_with_wrong_book(self):
        with self.assertRaises(Exception) as ex:
            wrong_role = {"name": "Mtsiri",
                          "type": "classic",
                          "book": "{}{}".format(base_url_book, str(random.randint(4000000000, 9120000001))),
                          "level": 1212
                          }
            add_new_item(base_url_role, wrong_role)
        self.assertEqual("Item hasn't been added", str(ex.exception))


class TestAddItemIdFunc(unittest.TestCase):
    def test_correct_addition(self):
        role = {"name": "Mtsiri",
                "type": "classic",
                "book": "http://pulse-rest-testing.herokuapp.com/books/6631",
                "level": 1212
                }
        add_item_id(role, 22)
        self.assertEqual(role["id"], 22)

    def test_correct_id_update(self):
        role = {"name": "Mtsiri",
                "type": "classic",
                "book": "http://pulse-rest-testing.herokuapp.com/books/6631",
                "level": 1212,
                "id": 22
                }
        add_item_id(role, 1)
        self.assertEqual(role["id"], 1)


class TestDictCompareFunc(unittest.TestCase):
    def setUp(self):
        self.dict1 = {"name": "Mtsiri", "type": "classic", "book": "http://pulse-rest-testing.herokuapp.com/books/6631", "level": 1212, "id": 22}
        self.dict2 = {"name": "Mtsiri", "type": "classic", "book": "http://pulse-rest-testing.herokuapp.com/books/6631", "level": 1212, "id": 22}
        self.dict3 = {"name": "Mtsiri", "type": "classic", "book": "http://pulse-rest-testing.herokuapp.com/books/6631", "level": 1212, "id": 14}

    def test_compare_equal(self):
        result = compare_dicts(self.dict1, self.dict2)
        self.assertIsNone(result)

    def test_compare_not_equal(self):
        with self.assertRaises(Exception) as ex:
            compare_dicts(self.dict2, self.dict3)
        self.assertEqual("Dicts are not equal", str(ex.exception))


class TestCheckNewItemRole(unittest.TestCase):
    def setUp(self):
        self.book_id = add_new_item(base_url_book, book_dict)
        self.base_url = base_url_role
        self.role_dict = role_dict
        role_dict["book"] = "{}{}".format(base_url_book, self.book_id)
        self.role_id = add_new_item(base_url_role, role_dict)

    def tearDown(self):
        delete_item_finally(base_url_book, self.book_id)
        delete_item_finally(base_url_role, self.role_id)

    def test_check_correct_data(self):
        result = check_new_item(base_url_role, self.role_id, role_dict)
        self.assertIsNone(result)

    def test_check_with_wrong_id(self):
        with self.assertRaises(Exception) as ex:
            check_new_item(base_url_role, str(random.randint(4000000000, 9120000001)), role_dict)
        self.assertEqual("Wrong request", str(ex.exception))

    def test_role_in_list(self):
        result = check_item_in_list(base_url_role, self.role_id, role_dict)
        self.assertIsNone(result)

    def test_role_in_list_wrong_id(self):
        with self.assertRaises(Exception) as ex:
            check_item_in_list(base_url_role, str(random.randint(4000000000, 9120000001)), role_dict)
        self.assertEqual("The item is not in the list", str(ex.exception))


class TestRoleUpdate(unittest.TestCase):
    def setUp(self):
        self.base_url = base_url_role
        self.book_id = add_new_item(base_url_book, book_dict)
        self.role_dict = role_dict
        role_dict["book"] = "{}{}".format(base_url_book, self.book_id)
        self.role_id = add_new_item(base_url_role, role_dict)

    def tearDown(self):
        delete_item_finally(base_url_book, self.book_id)
        delete_item_finally(base_url_role, self.role_id)

    def test_updated_data(self):
        result = role_update_and_check(base_url_role, self.role_id, role_dict, new_name=str(uuid.uuid4()),
                                       new_type=str(uuid.uuid4()), new_book=role_dict["book"], new_level=random.randint(40000000, 2147483647))
        self.assertIsNone(result)

    def test_update_one_parameter(self):
        result = role_update_and_check(base_url_role, self.role_id, role_dict, new_name="vova", new_book=role_dict["book"])
        self.assertIsNone(result)

    def test_update_attempt_wrong_id(self):
        with self.assertRaises(Exception) as ex:
            role_update_and_check(base_url_role, str(random.randint(4000000000, 9120000001)), role_dict,
                                           new_name=str(uuid.uuid4()), new_type=str(uuid.uuid4()))
        self.assertEqual("Wrong request", str(ex.exception))

    def test_attempt_update_wrong_url(self):
        with self.assertRaises(Exception) as ex:
            role_update_and_check(base_url_role+"wrong", str(random.randint(4000000000, 9120000001)), role_dict,
                                           new_name=str(uuid.uuid4()), new_type=str(uuid.uuid4()))
        self.assertEqual("Wrong request", str(ex.exception))


class TestDeleteItemFunc(unittest.TestCase):
    def setUp(self):
        self.base_url = base_url_role
        self.book_id = add_new_item(base_url_book, book_dict)
        self.role_dict = role_dict
        role_dict["book"] = "{}{}".format(base_url_book, self.book_id)
        self.role_id = add_new_item(base_url_role, role_dict)

    def tearDown(self):
        delete_item_finally(base_url_book, self.book_id)
        delete_item_finally(base_url_role, self.role_id)

    def test_delete_existent(self):
        new_test_id = add_new_item(base_url_role, role_dict)
        result = delete_item_finally(base_url_role, new_test_id)
        self.assertIsNone(result)

    def test_try_delete_with_id_none(self):
        with self.assertRaises(Exception) as ex:
            delete_item_finally(base_url_role, None)
        self.assertEqual("Item id is None", str(ex.exception))

    def test_try_delete_with_wrong_id(self):
        with self.assertRaises(Exception) as ex:
            delete_item_finally(base_url_role, str(random.randint(4000000000, 9120000001)))
        self.assertEqual("Wrong request status code. Item hasn't been deleted", str(ex.exception))



if __name__ == '__main__':
    from HtmlTestRunner import HTMLTestRunner
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output=r"C:\Users\user\workspace_python\Homeworks\Test_unit_test_Homework_7"))

    testCreate1 = TestAddNewRole("test_new_role_id_type")
    testCreate2 = TestAddNewRole("test_new_role_id_emptiness")
    testDelete = TestDeleteItemFunc("test_delete_existent")
    smoke_suite = unittest.TestSuite([testCreate1, testCreate2, testDelete])
    result = unittest.TestResult()
    smoke_suite.run(result)
    print(result)
