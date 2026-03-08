from google import genai
from google.genai import types
import time

class AIService:
    def __init__(self, api_key: str):
        # 初始化谷歌客户端
        self.client = genai.Client(api_key=api_key)

    def analyze_image_with_prompt(self, image_bytes: bytes, mime_type: str, prompt: str) -> str:
        """
        接收图片字节流、格式和指令，返回 AI 的文字点评。
        """
        try:
            # 1. 封装图片零件
            image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
            # 2. 封装文字零件
            text_part = types.Part.from_text(text=prompt)

            time.sleep(2)

            # 3. 发送给 Gemini 2.0 Flash
            response = self.client.models.generate_content(
                model='gemini-2.0-flash',
                contents=[text_part, image_part]
            )
            return response.text
        except Exception as e:
            return f"AI 视觉大脑暂时罢工，请稍后再试。(错误详情: {str(e)})"
