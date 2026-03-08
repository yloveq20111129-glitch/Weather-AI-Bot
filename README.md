# 📂 AI Photo Assistant - Backend API 📸🤖

这是一个基于 **FastAPI** 和 **Google Gemini 2.0 Flash** 构建的智能摄影指导后端系统。本项目不仅是一个 AI 助手，更是我从 API 调用者进化为后端架构师的技术里程碑。

---

### 📸 核心功能 (Core Features)

本项目专为摄影爱好者打造，具备以下技术亮点：

*   **👁️ 真正的多模态 (Multimodal) AI 视觉分析**：不仅能处理文字，还能直接“读懂”图片的二进制数据流。利用最新的 **Gemini 2.0 Flash** 模型，实现对照片构图、色彩、光影的全方位深度解析。
*   **⚡️ 高性能异步图片上传接口**：基于 **FastAPI** 框架构建，支持高并发处理。采用 HTTP 的 **POST** 方法接收文件流，并通过 `async` / `await` 异步非阻塞机制，确保在读取大图时服务器依然运行流畅。
*   **🛡️ 工业级健壮性与安全设计**：
    *   **安全屏障**：所有敏感 API Key 均通过 `.env` 文件进行环境隔离，并配合 `.gitignore` 严防密钥泄露。
    *   **容错机制**：内置 `try...except` 保护罩，针对 API 限流（429 报错）或网络异常实现优雅降级，返回体面的提示而非崩溃。

---

### 🛠️ 技术栈 (Tech Stack)

*   **编程语言**：Python 3.13+
*   **Web 框架**：FastAPI (构建高性能 RESTful API)
*   **异步服务器**：Uvicorn (发电机级驱动引擎)
*   **数据校验**：Pydantic (铁面无私的数据质检员)
*   **AI 引擎**：Google GenAI SDK (多模态视觉大脑)
*   **配置管理**：Python-dotenv (隐藏的保险箱读取器)

---

### 📂 目录结构 (Project Structure)

```text
.
├── main.py          # FastAPI 核心入口，负责定义路由(Route)和接收用户请求
├── ai_service.py    # AI 视觉核心逻辑模块，采用了 OOP (面向对象) 思想实现逻辑解耦
├── .env             # 存放敏感 API Key 的“保险箱”，已被 Git 忽略
├── .gitignore       # Git 屏蔽清单，确保密码不上传公网
└── README.md        # 本说明文档
```

---

### 🚀 快速启动 (Quick Start)

1. **配置环境**：
   在根目录创建 `.env` 文件并填入你的 Key：
   ```text
   AI_KEY=你的谷歌Gemini密钥
   ```

2. **启动后端服务**：
   ```bash
   python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **交互式测试**：
   访问 `http://localhost:8000/docs` 进入 Swagger UI，点击 `POST /analyze_photo` 即可上传照片获取 AI 建议。

---

### 🧠 技术感言 (Developer's Note)

本项目标志着我完成了从“写脚本”到“搭系统”的跨越。通过解决 401 (鉴权失败) 和 429 (频率受限) 等实战报错，我深刻理解了 **HTTP 协议** 的精髓。正如本项目代码结构所展示的：**后端开发的灵魂不在于写代码，而在于设计数据流动的规矩。**


---
