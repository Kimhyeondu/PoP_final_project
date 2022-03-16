import tempfile
from PIL import Image

from django.db import connection
from django.test import TestCase, override_settings
from django.test.utils import CaptureQueriesContext
from django.core.files.uploadedfile import SimpleUploadedFile

from pop_final_project.settings import  MEDIA_ROOT
from card.services.gift_service import *
from card.models import Gift, Message
from asgiref.sync import sync_to_async, async_to_sync

# CRUD - create,get,filter,update,delete
class TestGiftService(TestCase):

    @override_settings(MEDIA_ROOT = tempfile.TemporaryDirectory(prefix='mediatest').name)
    def test_gift_create(self):
        gift_name = "sample_name"
        gift_img = SimpleUploadedFile(name='logo.png', content=open("./static/img/logo.png",'rb').read(), content_type='image/png')
        gift_desc = "sample_description"
        tags = "다이어트, 요리, 골프"
        with self.assertNumQueries(42):
            new_gift = async_to_sync(gift_create)(gift_name=gift_name, gift_img=gift_img, gift_desc=gift_desc, tags=tags)
            self.assertEqual(new_gift.gift_name, gift_name)
            self.assertEqual(new_gift.gift_img, gift_img)
            self.assertEqual(new_gift.gift_desc, gift_desc)
            db_tags = list(new_gift.tags.names())
            self.assertEqual(len(db_tags), 3)
            tags_list = list(map(lambda x: x.strip(), tags.strip().split(",")))
            self.assertEqual(sorted(db_tags), sorted(tags_list))


    @override_settings(MEDIA_ROOT = tempfile.TemporaryDirectory(prefix='mediatest').name)
    def test_gift_get(self):
        gift_name = "sample_name"
        gift_img = SimpleUploadedFile(name='logo.png', content=open("./static/img/logo.png",'rb').read(), content_type='image/png')
        gift_desc = "sample_description"
        tags = "다이어트"
        async_to_sync(gift_create)(gift_name=gift_name, gift_img=gift_img, gift_desc=gift_desc, tags=tags)
        with self.assertNumQueries(2):
            new_gift = async_to_sync(gift_get)(id = 1)
            self.assertEqual(new_gift.gift_name, gift_name)
            self.assertEqual(new_gift.gift_img, gift_img)
            self.assertEqual(new_gift.gift_desc, gift_desc)
            db_tags = list(new_gift.tags.names())
            self.assertEqual(len(db_tags), 1)
            tags_list = list(map(lambda x: x.strip(), tags.strip().split(",")))
            self.assertEqual(sorted(db_tags), sorted(tags_list))


    @override_settings(MEDIA_ROOT = tempfile.TemporaryDirectory(prefix='mediatest').name)
    def test_gift_list_all(self):
        for i in range(5):
            gift_name = "test"+str(i)
            gift_img = SimpleUploadedFile(name='logo.png', content=open("./static/img/logo.png",'rb').read(), content_type='image/png')
            gift_desc = "sample_description"
            tags = "다이어트"
            async_to_sync(gift_create)(gift_name=gift_name, gift_img=gift_img, gift_desc=gift_desc, tags=tags)
        with self.assertNumQueries(1):
            gift_list = async_to_sync(gift_list_all)()
            self.assertEqual(5, len(gift_list))
            for i in range(5):
                self.assertEqual(gift_list[i].gift_name, "test{}".format(str(i)))


    @override_settings(MEDIA_ROOT = tempfile.TemporaryDirectory(prefix='mediatest').name)
    def test_gift_list_by_filter(self):
        for i in range(3):
            gift_name = "test"+str(i)
            gift_img = SimpleUploadedFile(name='logo.png', content=open("./static/img/logo.png",'rb').read(), content_type='image/png')
            gift_desc = "sample_description"
            tags = "다이어트"
            async_to_sync(gift_create)(gift_name=gift_name, gift_img=gift_img, gift_desc=gift_desc, tags=tags)
        for i in range(3,7):
            gift_name = "test"+str(i)
            gift_img = SimpleUploadedFile(name='logo.png', content=open("./static/img/logo.png",'rb').read(), content_type='image/png')
            gift_desc = "sample_description"
            tags = "골프"
            async_to_sync(gift_create)(gift_name=gift_name, gift_img=gift_img, gift_desc=gift_desc, tags=tags)
        with self.assertNumQueries(3):
            gift_list_all = async_to_sync(gift_list_by_filter)(tags__name__in=["다이어트", "골프"])
            gift_list_1 = async_to_sync(gift_list_by_filter)(tags__name__in=["다이어트"])
            gift_list_2 = async_to_sync(gift_list_by_filter)(tags__name="골프")
            self.assertEqual(7, len(gift_list_all))
            self.assertEqual(3, len(gift_list_1))
            self.assertEqual(4, len(gift_list_2))
            for i in range(3):
                self.assertEqual(gift_list_1[i].gift_name, "test{}".format(str(i)))


    @override_settings(MEDIA_ROOT = tempfile.TemporaryDirectory(prefix='mediatest').name)
    def test_gift_list_by_search(self):
        for i in range(3):
            gift_name = "test"+str(i)
            gift_img = SimpleUploadedFile(name='logo.png', content=open("./static/img/logo.png",'rb').read(), content_type='image/png')
            gift_desc = "sample_description"
            tags = "다이어트"
            async_to_sync(gift_create)(gift_name=gift_name, gift_img=gift_img, gift_desc=gift_desc, tags=tags)
        for i in range(3,7):
            gift_name = "test"+str(i)
            gift_img = SimpleUploadedFile(name='logo.png', content=open("./static/img/logo.png",'rb').read(), content_type='image/png')
            gift_desc = "sample_description"
            tags = "골프"
            async_to_sync(gift_create)(gift_name=gift_name, gift_img=gift_img, gift_desc=gift_desc, tags=tags)
        with self.assertNumQueries(3):
            gift_list_all = async_to_sync(gift_list_by_search)("test")
            gift_list_1 = async_to_sync(gift_list_by_search)("다이어트")
            gift_list_2 = async_to_sync(gift_list_by_search)("골프")
            self.assertEqual(7, len(gift_list_all))
            self.assertEqual(3, len(gift_list_1))
            self.assertEqual(4, len(gift_list_2))
            for i in range(3):
                self.assertEqual(gift_list_1[i].gift_name, "test{}".format(str(i)))


    def test_gift_update(self):
        pass

    def test_gift_delete(self):
        pass
