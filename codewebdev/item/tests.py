from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from decimal import Decimal
from .models import Category, Item


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Casual')
    
    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Casual')
        self.assertEqual(str(self.category), 'Casual')
    
    def test_category_ordering(self):
        Category.objects.create(name='Formal')
        Category.objects.create(name='Athletic')
        categories = Category.objects.all()
        self.assertEqual(categories[0].name, 'Athletic')
        self.assertEqual(categories[1].name, 'Casual')


class ItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Casual')
        self.item = Item.objects.create(
            category=self.category,
            name='Test T-Shirt',
            description='A test t-shirt',
            price=Decimal('29.99'),
            original_price=Decimal('49.99'),
            rating=Decimal('4.5'),
            created_by=self.user
        )
    
    def test_item_creation(self):
        self.assertEqual(self.item.name, 'Test T-Shirt')
        self.assertEqual(self.item.price, Decimal('29.99'))
        self.assertEqual(str(self.item), 'Test T-Shirt')
    
    def test_discount_percentage(self):
        discount = self.item.discount_percentage
        self.assertEqual(discount, 40)  # 40% off
    
    def test_discount_percentage_no_original_price(self):
        item = Item.objects.create(
            category=self.category,
            name='No Discount Item',
            price=Decimal('29.99'),
            created_by=self.user
        )
        self.assertEqual(item.discount_percentage, 0)
    
    def test_item_is_not_sold_by_default(self):
        self.assertFalse(self.item.is_sold)


class ItemViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Casual')
        self.item = Item.objects.create(
            category=self.category,
            name='Test T-Shirt',
            description='A test t-shirt',
            price=Decimal('29.99'),
            rating=Decimal('4.5'),
            created_by=self.user
        )
    
    def test_items_view(self):
        response = self.client.get(reverse('item:items'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test T-Shirt')
        self.assertTemplateUsed(response, 'item/items.html')
    
    def test_items_view_with_search(self):
        response = self.client.get(reverse('item:items') + '?query=T-Shirt')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test T-Shirt')
    
    def test_items_view_with_category_filter(self):
        response = self.client.get(
            reverse('item:items') + f'?category={self.category.id}'
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test T-Shirt')
    
    def test_detail_view(self):
        response = self.client.get(
            reverse('item:detail', kwargs={'pk': self.item.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test T-Shirt')
        self.assertTemplateUsed(response, 'item/detail.html')
    
    def test_new_item_view_requires_login(self):
        response = self.client.get(reverse('item:new'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_new_item_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('item:new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/form.html')
    
    def test_edit_item_view_requires_owner(self):
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        self.client.login(username='otheruser', password='testpass123')
        response = self.client.get(
            reverse('item:edit', kwargs={'pk': self.item.pk})
        )
        self.assertEqual(response.status_code, 404)
    
    def test_delete_item(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('item:delete', kwargs={'pk': self.item.pk})
        )
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertFalse(Item.objects.filter(pk=self.item.pk).exists())


class ItemFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Casual')
    
    def test_create_item_via_form(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('item:new'), {
            'category': self.category.id,
            'name': 'New T-Shirt',
            'description': 'Brand new t-shirt',
            'price': '39.99',
            'rating': '4.0',
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertTrue(Item.objects.filter(name='New T-Shirt').exists())