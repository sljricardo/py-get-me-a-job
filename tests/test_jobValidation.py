import unittest

from src.Job import Job

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

if __name__ == '__main__':
    unittest.main()