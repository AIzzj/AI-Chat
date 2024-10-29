# AI 创作助手

AI 创作助手是一个结合了音乐生成、图像处理和自然语言处理的创意工具。它使用先进的AI模型来辅助用户进行各种创意活动。

## 功能

- 音乐生成：基于文字描述生成音乐
- 图像处理：（待实现）
- 自然语言处理：使用 ERNIE-Bot 进行对话（待实现）

## 安装

1. 克隆仓库：
   ```
   git clone https://github.com/your-username/ai-creative-assistant.git
   cd ai-creative-assistant
   ```

2. 创建并激活虚拟环境：
   ```
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 使用说明

1. 启动 Flask 服务器：
   ```
   python creative_spirit.py
   ```

2. 访问 http://localhost:5000 来使用 Web 界面。

3. 使用 API：
   - 生成音乐：
     ```
     curl -X POST -H "Content-Type: application/json" -d '{"description":"A happy melody", "duration":10}' http://localhost:5000/generate_music
     ```

## 开发

- 运行测试：
  ```
  python -m unittest discover tests
  ```

## 贡献

欢迎提交 Pull Requests 来改进这个项目。对于重大更改，请先开 issue 讨论您想要改变的内容。

## 许可

[MIT](https://choosealicense.com/licenses/mit/)

