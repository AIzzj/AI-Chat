import os

# 音乐生成配置
MUSIC_GEN_MODEL = 'facebook/musicgen-small'
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'generated_music')

# Flask 配置
DEBUG = True

# 日志配置
LOG_LEVEL = 'INFO'
LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs', 'app.log')

# 确保日志目录存在
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# ... 其他配置 ...
