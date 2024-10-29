#!/bin/bash

# 拉取最新代码
git pull

# 构建 Docker 镜像
docker-compose build

# 停止旧容器
docker-compose down

# 启动新容器
docker-compose up -d

echo "Deployment completed successfully!"
