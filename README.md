# Dockerfile for Numerai Submit

## Setup

1. Put `*.ipynb` and `model/*`
2. setup `.env`
3. `make`
4. `make run`

## 説明

Dockerfileでは、このフォルダ直下に置いた `*.ipynb` と `model` フォルダをDockerイメージにコピーします。
docker run すると`*.ipynb`を順番に実行してくれます。
成功もしくは失敗するとDiscordに通知が飛びます。
