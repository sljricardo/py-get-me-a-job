import unittest
import os

from src.Job import Job
from src.DB import DB

class TestJobs(unittest.TestCase):

    def test_if_provide_an_invalid_job_assert_fail(self):
        invalid_job_offer = {
            "title": "Full Stack Ruby Developer",
            "description": "We need a full stack web developer in Ruby on Rails and..."
        }
        self.assertFalse(Job(invalid_job_offer).isValid())

    def test_if_provide_a_valid_job_assert_true(self):
        valid_job_offer = {
            "title": "Full Stack Php Developer",
            "description": "We need a full stack web developer in Php and javascript and..."
        }
        self.assertTrue(Job(valid_job_offer).isValid())

    def test_if_provide_a_job_with_invalid_words_and_valid_words_assert_fail(self):
        job_offer = {
            "title": "Full Stack Vue Developer",
            "description": "We need a full stack web developer in rails and..."
        }
        self.assertFalse(Job(job_offer).isValid())

    def test_assert_to_see_job_offer_if_valid(self):
        job_offer = {
            "title": "Full Stack Vue Developer",
            "description": "We need a full stack web developer in php and...",
            "location": "empty",
            "company": "company_name",
            "company_logo": "http://www....",
            "url": "http://www..."
        }
        self.assertIn("New Job", Job(job_offer).info())

    def test_if_job_already_exists_in_db_assert_true(self):
        db = DB(os.path.abspath('store-test'))
        db.add('uid-test', { "title": "Php dev", "description": "dev php" })

        self.assertTrue(db.hasKey('uid-test'))
        # Aflter assertion remove file
        os.remove('store-test')

if __name__ == '__main__':
    unittest.main()