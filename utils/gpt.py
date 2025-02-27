from openai import OpenAI
from decouple import config

from core.models import ChatMessage

client = OpenAI(
    api_key=config("OPENAI_KEY")
)

# Global Variables
SYSTEM_CONTENT = '''
             شما یک دستیار هوشمند و حرفه‌ای سفر به دبی هستید که کاربر را راهنمایی می‌کنید تا بهترین تجربه را داشته باشد.
 پاسخ‌های خود را در قالب HTML ارائه دهید:
   - عنوان‌ها را با <h4> نمایش بده.
   - هر خط جدید را با <br> جدا کن.
   - متن‌ها را درون <p> قرار بده.
 فقط در مورد سفر به دبی، هتل‌ها، پروازها، تورها و فرصت‌های تجاری در دبی پاسخ بده.
 کاربر را به رزرو خدمات سفر از **DubaiBy** تشویق کن و بگو که می‌تواند همه رزروها را در سایت انجام دهد.
 همیشه **برند DubaiBy** را در پیام‌های خود بگنجان و از عبارت‌هایی مثل **"DubaiBy بهترین پیشنهادات را دارد!"** استفاده کن.
 حس فوریت و تخفیف را ایجاد کن؛ مثلاً بگو **"همین حالا با تخفیف ویژه رزرو کنید!"**.
 در پایان هر پیام یک CTA قوی بگذار که کاربر را به سایت هدایت کند.
 پیام‌های چت‌بات باید لحن دوستانه، صمیمی و جذاب داشته باشند تا کاربر را درگیر نگه دارد.
 اطلاعات جامع و به‌روز درباره سفر به دبی بده، از جمله:
   - **تورهای پیشنهادی** با قیمت‌های ویژه
   - **بهترین هتل‌ها** برای اقامت لوکس یا اقتصادی
   - **پروازهای مستقیم** با بهترین قیمت
   - **تفریحات و جاذبه‌های خاص دبی** که نباید از دست بدهد
 برای رزرو و اطلاعات بیشتر، همیشه کاربر را به سایت **DubaiBy** هدایت کن:
    <a href="/">رزرو از DubaiBy</a>

'''


def get_last_5_messages(user_id):
    """Latest user message"""
    if user_id:
        messages = ChatMessage.objects.filter(user_id=user_id)[:20]

        conversation = []
        for msg in reversed(messages):
            conversation.append({"role": "user", "content": msg.user_message})
            conversation.append({"role": "assistant", "content": msg.bot_message})

        return conversation
    return []


def gpt_request(system_prompt, user_prompt, user_id):
    conversation = get_last_5_messages(user_id)

    conversation.insert(0, {"role": "system", "content": system_prompt})

    conversation.append({"role": "user", "content": user_prompt})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation
    )

    assistant_message = response.choices[0].message.content

    return assistant_message
