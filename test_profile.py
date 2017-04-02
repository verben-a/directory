import unittest
import os
import json

os.environ["CONFIG_PATH"] = "directory.config.TestConfig"

from directory import app
from directory import models
# content-providers -> s3, akamai, CDNs
from directory.database import Base, session, engine


class TestProfile(unittest.TestCase):

	def setUp(self):
		Base.metadata.create_all(engine)

		self.user = models.User()

		# self.profile = ??/

	def tearDown(self):
		session.close()
		# Remove the tables and their data from the database
		Base.metadata.drop_all(engine)

        # Delete test upload folder
        # shutil.rmtree(upload_path())



	def test_profile_creation(self):
		self.assertEqual(self.user.username, 'alina');



if __name__ == "__main__":
    unittest.main()
