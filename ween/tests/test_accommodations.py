import pytest
from flask import Flask, render_template_string

# إنشاء تطبيق Flask تجريبي
app = Flask(__name__)

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        with app.app_context():
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

# ✅ اختبار ناجح: يجب أن يمر
def test_render_template_pass():
    data = [
        {"name": "Luxury Hotel", "price": 500},
        {"name": "Budget Hostel", "price": 80},
    ]
    
    with app.app_context():
        rendered = render_template_string(TEMPLATE, accommodations=data)
    
    assert "Luxury Hotel" in rendered
    assert "Premium" in rendered
    assert "Budget Hostel" in rendered
    assert "Standard" in rendered

# ❌ اختبار فاشل عمدًا: يجب أن يفشل لإظهار الفشل في `GitHub Actions`
def test_render_template_fail():
    data = [
        {"name": "Luxury Hotel", "price": 500},
    ]
    
    with app.app_context():
        rendered = render_template_string(TEMPLATE, accommodations=data)
    
    assert "Non-Existent Hotel" in rendered  # 🔹 هذا الشرط سيفشل دائمًا
