# 登入入口網站
現在只有後端，前端未上傳(目前前端為測試用)

## Usage

```
pip install -r requirements.txt
```

## environment variables

```
SECRET_KEY=
ALGORITHM=

ACCESS_TOKEN_EXPIRE_MINUTES=
REFRESH_TOKEN_EXPIRE_DAYS=

DATABASE=

HOST=127.0.0.1
PORT=8000
```

# Frontend Setup Guide (npm)

本文件說明如何在 **全新環境（未安裝任何前端工具）** 下，  
建置並啟動本專案的前端（Next.js + npm）。

---

## 1. 安裝 Node.js

請先安裝 **Node.js（LTS 版本）**  
https://nodejs.org

安裝完成後，開啟 Terminal（或命令提示字元）檢查：

```bash
node --version
npm --version
```

## 2. 建制相關環境
```
cd frontend
npm install
```

## 3. 啟動前端
```
npm run dev
```
瀏覽器開啟
```
http://localhost:3000
```
