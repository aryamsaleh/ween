import pytest
from flask import Flask, render_template_string

# إنشاء تطبيق Flask تجريبي
app = Flask(__name__)

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        with app.app_context():  # 🔹 إضافة هذا لإصلاح الخطأ
            yield client

# كود القالب الذي نريد اختباره
TEMPLATE = """
{% for accommodation in accommodations %}
    <h5>{{ accommodation.name }}</h5>
    {% if accommodation.price > 400 %}
        <span>Premium</span>
    {% else %}
        <span>Standard</span>
    {% endif %}
{% endfor %}
"""

def test_render_template():
    data = [
        {"name": "Luxury Hotel", "price": 500},
        {"name": "Budget Hostel", "price": 80},
    ]
    
    with app.app_context():  # 🔹 إضافة هذا لحل المشكلة
        rendered = render_template_string(TEMPLATE, accommodations=data)
    
    assert "Luxury Hotel" in rendered
    assert "Premium" in rendered
    assert "Budget Hostel" in rendered
    assert "Standard" in rendered
