from locust import HttpUser, task, between

class AIAssistantUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def generate_music(self):
        self.client.post("/generate_music", json={
            "description": "A happy melody",
            "duration": 5
        })

    @task
    def chat(self):
        self.client.post("/chat", json={
            "bot_id": 1,
            "message": "Hello, how are you?"
        })

# 运行命令: locust -f locustfile.py
