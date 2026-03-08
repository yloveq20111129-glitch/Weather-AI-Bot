from fastapi import FastAPI,File,UploadFile
from pydantic_settings import BaseSettings,SettingsConfigDict
from ai_service import AIService

#1.配置加载（保持不变）
class Settings(BaseSettings):
	AI_KEY: str
	model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

#2.初始化APP和AI大脑
app = FastAPI(title="AI拍照助手后端")
ai_brain = AIService(api_key=settings.AI_KEY) #创建一个AI服务实例（并未运行功能）

#---接口部分---
@app.get("/")
def home():
	return{"status":"AI服务已启动"}

@app.post("/analyze_photo")
async def analyze_photo(file:UploadFile = File(...)):
	#读取文档内容
	contents = await file.read()

	#构建指令
	prompt = """你是一位专业的摄影导师。请分析这张照片的构图、光影、情绪和色彩，
    并给出3条具体的改进建议，让照片更有电影感。请用中文回答。"""

	print(f"🤖 正在把图片 {file.filename} 转发给 AI 服务...")

	# 【核心变化】：不再自己调用 client，而是直接使唤 ai_brain
	ai_comment = ai_brain.analyze_image_with_prompt(image_bytes=contents,mime_type=file.content_type,prompt=prompt)

	return{"文件名":file.filename,
		"AI_摄影建议":ai_comment,
		"状态":"分析完成"
	}
