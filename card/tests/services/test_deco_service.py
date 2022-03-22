import os
import shutil
import tempfile
from PIL import Image

from django.test import TestCase, override_settings, TransactionTestCase
from django.core.files.uploadedfile import SimpleUploadedFile, UploadedFile

from pop_final_project.settings import BASE_DIR, MEDIA_ROOT
from card.services.deco_service import *
from card.models import Gift, Message, Decoration
from asgiref.sync import sync_to_async, async_to_sync

TEST_DIR = os.path.join(BASE_DIR, "test_data")

def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'png')
    return temp_file



@override_settings(MEDIA_ROOT = (TEST_DIR + '/media'))
class TestDecorationService(TransactionTestCase):
    reset_sequences = True

    def test_create_deco(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file).name
        # test_image = SimpleUploadedFile(name='logo.png', content=open("./static/img/logo.png",'rb').read(), content_type='image/png')
        deco_name = "test_deco"
        deco_img = test_image
        try:
            with self.assertNumQueries(1):
                new_deco = async_to_sync(create_deco)(deco_name=deco_name, deco_img=deco_img)
                self.assertEqual(new_deco.deco_name, deco_name)
                self.assertEqual(new_deco.deco_img, deco_img)
                
        finally:
            tearDownModule()

    def test_get_deco(self):
        pass
            
    def test_all_list_deco(self):
        pass

    def delete_deco(self):
        pass


def tearDownModule():
    # print("\n Deleting temporary files...\n")
    try:
        shutil.rmtree(TEST_DIR)
    except OSError:
        pass
