#!/bin/bash

# 更新並安裝必要的軟體包
sudo apt update
sudo apt install -y git curl ca-certificates lzip python3 python3-pip wl-clipboard xclip waydroid

# 安裝 Python 依賴
sudo pip install pyclip --break-system-packages
sudo pip install cloudscraper --break-system-packages
sudo pip install tqdm --break-system-packages

# 安裝 Waydroid
curl https://repo.waydro.id | sudo bash
sudo waydroid init

# 啟動 Waydroid 服務
sudo systemctl start waydroid-container
waydroid session start
waydroid prop set persist.waydroid.multi_windows true
waydroid session stop
waydroid session start
sudo systemctl enable waydroid-container

# 下載並安裝 Gboard 和 Ogden APK
python3 downloadGboard.py
waydroid app install gboard.apk
waydroid app install ogden.apk

# 安裝 Waydroid Script
cd ~
git clone https://github.com/casualsnek/waydroid_script
cd waydroid_script
python3 -m venv venv
venv/bin/pip install -r requirements.txt

# 執行 Waydroid Script
sudo venv/bin/python3 main.py
/bin/python3 main.py

# 完成安裝
echo "Waydroid 與 Gboard 安裝完成！"
