import os
import shutil
import tempfile
from PIL import Image

from django.test import TestCase, override_settings, TransactionTestCase

from pop_final_project.settings import BASE_DIR, MEDIA_ROOT
from card.services.deco_service import *
from card.models import Gift, Message, Decoration
from asgiref.sync import sync_to_async, async_to_sync

# view get,post,etc 정상작동 확인 

TEST_DIR = os.path.join(BASE_DIR, "test_data")


def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'png')
    return temp_file


@override_settings(MEDIA_ROOT = (TEST_DIR + '/media'))
class TestCardView(TestCase):
    
    def test_GET_card_write(self):
        pass


    def test_POST_card_write(self):
        pass


    def test_Wrong_card_write(self):
        pass


def tearDownModule():
    # print("\n Deleting temporary files...\n")
    try:
        shutil.rmtree(TEST_DIR)
    except OSError:
        pass
