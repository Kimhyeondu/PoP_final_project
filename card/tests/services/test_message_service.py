import os
import shutil
from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile

from card.services.message_service import *
from user.models import User
from card.models import Gift, Message
from pop_final_project.settings import BASE_DIR, MEDIA_ROOT

# CRUD - create,get,filter,update,delete
TEST_DIR = os.path.join(BASE_DIR, "test_data")

class TestMessageService(TestCase):

    @override_settings(MEDIA_ROOT = (TEST_DIR + '/media'))
    def test_msg_create(self):
        from_user = 1
        to_user = 2
        gift = 1
        msg = "test_msg"
        deco = "1"


        pass

    def test_msg_get(self):
        pass

    def test_msg_list(self):
        pass

    def test_msg_update(self):
        pass

    def test_msg_delete(self):
        pass


def tearDownModule():
    # print("\n Deleting temporary files...\n")
    try:
        shutil.rmtree(TEST_DIR)
    except OSError:
        pass
