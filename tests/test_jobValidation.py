import unittest
import os

from Job import Job
from DB import DB


class TestJobs(unittest.TestCase):

    def test_if_provide_an_invalid_job_assert_fail(self):
        invalid_job_offer = {
            "content": "Full Stack Ruby Developer",
            "uid": "test"
        }
        self.assertFalse(Job(invalid_job_offer).isValid())

    def test_if_provide_a_valid_job_assert_true(self):
        valid_job_offer = {
            "content": "Full Stack Php Developer",
            "uid": "test"
        }
        self.assertTrue(Job(valid_job_offer).isValid())

    def test_if_provide_a_job_with_invalid_words_and_valid_words_assert_fail(self):
        job_offer = {
            "content": "Full Stack Vue Developer and Ruby",
            "uid": "test"
        }
        self.assertFalse(Job(job_offer).isValid())

    def test_if_job_already_exists_in_db_assert_true(self):
        db = DB(os.path.abspath('store-test'))
        db.add('uid-test', {"title": "Php dev", "description": "dev php"})

        self.assertTrue(db.hasKey('uid-test'))
        # Aflter assertion remove file
        os.remove('store-test')


if __name__ == '__main__':
    unittest.main()
