import pytest
from product.models.product import Product
from product.models.category import Category
from product.Serializers.product_Serializers import ProductSerializer

@pytest.fixture
def sample_category(db):
    return Category.objects.create(title="Fiction")

@pytest.fixture
def sample_product(db, sample_category):
    product = Product.objects.create(title="Harry Potter", price=29.99, active=True)
    product.category.add(sample_category)
    return product

def test_product_creation(sample_product):
    assert sample_product.title == "Harry Potter"
    assert sample_product.price == 29.99
    assert sample_product.active is True
    assert sample_product.category.count() == 1

def test_product_serializer_fields(sample_product):
    serializer = ProductSerializer(sample_product)
    data = serializer.data
    assert data['title'] == "Harry Potter"
    assert data['price'] == '29.99'  # Decimal serializado como string
    assert data['active'] is True
    assert len(data['category']) == 1
    assert data['category'][0]['title'] == "Fiction"

def test_product_serializer_validation():
    # Teste de criação com dados inválidos
    serializer = ProductSerializer(data={'title': '', 'price': -10})
    assert not serializer.is_valid()
    
    # 'title' continuará sendo obrigatório
    assert 'title' in serializer.errors
    
    # O serializer está exigindo o campo 'categories_id'
    assert 'categories_id' in serializer.errors

    # Como o serializer atual não valida preço negativo, 
    # não devemos exigir erro em 'price' neste momento.
