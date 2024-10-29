import streamlit as st
import openai
import sqlite3
import random

# 设置OpenAI API密钥
openai.api_key = "your-api-key-here"

# 创建数据库连接
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# 创建用户表
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT UNIQUE,
              preferences TEXT)''')
conn.commit()

def get_ai_response(prompt, max_tokens=150):
    """
    使用OpenAI API获取AI响应
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"发生错误：{str(e)}"

def save_user_preferences(username, preferences):
    """
    保存用户偏好到数据库
    """
    c.execute("INSERT OR REPLACE INTO users (username, preferences) VALUES (?, ?)",
              (username, preferences))
    conn.commit()

def get_user_preferences(username):
    """
    从数据库获取用户偏好
    """
    c.execute("SELECT preferences FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    return result[0] if result else None

def main():
    st.title("AI创作助手")

    # 用户登录
    username = st.text_input("请输入您的用户名：")
    if username:
        preferences = get_user_preferences(username)
        if not preferences:
            st.info("欢迎新用户！请告诉我们您的偏好。")
            preferences = st.text_area("请输入您的创作偏好（如喜欢的风格、主题等）：")
            if preferences:
                save_user_preferences(username, preferences)
        else:
            st.success(f"欢迎回来，{username}！")

    # 创作类型选择
    creation_type = st.selectbox(
        "请选择创作类型",
        ["绘画", "视频", "游戏", "其他"]
    )

    # 用户输入
    user_input = st.text_area("请描述您的创作想法：")

    if st.button("获取AI建议"):
        if user_input:
            prompt = f"用户{username}想要创作{creation_type}。他们的想法是：{user_input}\n"
            if preferences:
                prompt += f"用户的偏好是：{preferences}\n"
            prompt += "请提供一些创意建议和下一步操作指导。"
            ai_response = get_ai_response(prompt, max_tokens=300)
            st.write("AI建议：", ai_response)
        else:
            st.warning("请输入您的创作想法。")

    # 创作指导
    if st.button("获取创作指导"):
        platforms = {
            "绘画": ["DeviantArt", "ArtStation", "Behance"],
            "视频": ["YouTube", "Vimeo", "TikTok"],
            "游戏": ["Steam", "itch.io", "GameJolt"],
            "其他": ["Medium", "WordPress", "Tumblr"]
        }
        selected_platform = random.choice(platforms[creation_type])
        prompt = f"请提供在{selected_platform}平台上注册账号并发布{creation_type}作品的详细步骤指南。"
        guide = get_ai_response(prompt, max_tokens=500)
        st.write("创作指导：", guide)

    # 添加聊天历史
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("您还有什么问题吗？"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            ai_response = get_ai_response(prompt)
            st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    main()
