from models import IdeaSchema, validate_idea_content, transform_idea_to_preview
from datetime import datetime
from contextlib import contextmanager

# طبقة المنطق 

@contextmanager 
def logic_processing_context(idea_input: IdeaSchema):
    """
    Context Manager لضمان معالجة الفكرة بشكل آمن ومنفصل.
    """
    try:
        # 1. التحقق من منطق العمل (Custom Business Logic)
        if not validate_idea_content(idea_input):
            raise ValueError("Invalid logic: Title and Description are identical.")
        
        # 2. تحويل البيانات (Data Transformation)
        # نستخدم الدالة التي عرفناها في الـ Models للحصول على الـ summary و tools_count
        preview = transform_idea_to_preview(idea_input)
        
        # 3. بناء الرد النهائي (Final Payload)
        full_payload = {
            **preview,
            "category": idea_input.category.value,
            "created_at": datetime.now().isoformat(),
            "metadata": {
                "source": "Idea-Catch-API",

                "version": "1.0"
            }
        }
        yield full_payload
        
    except Exception as e:
        # رفع الخطأ ليتعامل معه الـ Global Error Handler في main.py
        raise e
    finally:
        # مساحة فارغة لأي عمليات تنظيف أو Logging مستقبلية
        pass

def execute_create_idea(idea_data: IdeaSchema):
    """
    الدالة التي سيتم استدعاؤها من الـ Controller (main.py).
    """
    with logic_processing_context(idea_data) as processed:
        return processed
