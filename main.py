
from fastapi import FastAPI, HTTPException, status
from models import IdeaSchema  # استيراد الهيكل
from logic import execute_create_idea # استيراد المنطق

# إنشاء كائن التطبيق (هذا هو السيرفر)
app = FastAPI()

# 1. تعريف مسار POST (لإرسال فكرة جديدة)
@app.post("/ideas/", status_code=status.HTTP_201_CREATED)
async def create_idea(idea_input: IdeaSchema):
    """
    هنا يحدث الـ Request (المستقبل هو idea_input)

    والـ Validation التلقائي يتم عبر IdeaSchema
    """
    try:
        # استدعاء الـ Logic لمعالجة البيانات
        # الـ Context Manager يعمل هنا بالخفاء داخل الدالة
        processed_data = execute_create_idea(idea_input)
        
        # الـ Response بصيغة JSON
        return {
            "status": "success",
            "data": processed_data
        }
        
    except ValueError as ve:
        # الـ Error Handling (تحويل خطأ المنطق لـ Status Code 400)
        raise HTTPException(  status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(ve)
        )
