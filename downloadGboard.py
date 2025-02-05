import cloudscraper
import shutil
from pathlib import Path
from tqdm import tqdm

# 定義 Gboard 的 APK 檔名
APK_PATH = Path("gboard.apk")


def download_gboard_apk():
    """從 APKPure 下載最新的 Gboard APK"""
    
    url = "https://d.apkpure.com/b/APK/com.google.android.inputmethod.latin?version=latest"
    
    print(f"Constructed URL: {url}")  # 調試輸出 URL
    
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, stream=True)
    
    print(f"Response Status Code: {response.status_code}")  # 調試輸出回應碼
    
    if not response.headers.get("content-type", "").startswith("application"):
        raise RuntimeError("Gboard is not available on APKPure.")
    
    with tqdm.wrapattr(
        response.raw,
        "read",
        desc="Downloading Gboard APK",
        total=int(response.headers.get("content-length", 0)),
    ) as r_raw:
        with open(APK_PATH, "wb") as f:
            shutil.copyfileobj(r_raw, f)
    
    print(f"Gboard APK downloaded to: {APK_PATH}")
    return APK_PATH

APK_PATH_Word = Path("ogden.apk")
def download_word_apk():
    """從 APKPure 下載最新的 Gboard APK"""
    
    url = "https://d.apkpure.com/b/APK/com.ogden.memo?version=latest"
    
    print(f"Constructed URL: {url}")  # 調試輸出 URL
    
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, stream=True)
    
    print(f"Response Status Code: {response.status_code}")  # 調試輸出回應碼
    
    if not response.headers.get("content-type", "").startswith("application"):
        raise RuntimeError("ogden is not available on APKPure.")
    
    with tqdm.wrapattr(
        response.raw,
        "read",
        desc="Downloading ogden APK",
        total=int(response.headers.get("content-length", 0)),
    ) as r_raw:
        with open(APK_PATH_Word, "wb") as f:
            shutil.copyfileobj(r_raw, f)
    
    print(f"ogden APK downloaded to: {APK_PATH_Word}")
    return APK_PATH_Word

if __name__ == "__main__":
    download_gboard_apk()
    download_word_apk()
