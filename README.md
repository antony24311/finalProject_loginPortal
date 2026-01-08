# 登入入口網站
現在只有後端，前端未上傳(目前前端為測試用)

## Usage

```
pip install -r requirements.txt
```
## 安裝 Node.js
請先安裝 Node.js（LTS 版本）
https://nodejs.org

安裝完成後，開啟 Terminal（或命令提示字元）檢查：

node --version
npm --version
## environment variables
.env from backend:
```
SECRET_KEY=
ALGORITHM=

ACCESS_TOKEN_EXPIRE_MINUTES=
REFRESH_TOKEN_EXPIRE_DAYS=

DATABASE=

HOST=127.0.0.1
PORT=8000
```
.env.local from frontend:
```
BACKEND_URL=http://backend:4000
NODE_ENV=development   
```
## start
```
docker compose up -d --build
```
mac:
```
open http://localhost:5600
```
windows:
```
start http://localhost:5600
```
