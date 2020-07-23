from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_default_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    
    def test_item_return_method_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEquals(str(item), 'Test Todo Item')
