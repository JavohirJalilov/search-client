import requests
import base64
import json
import sys
import os

def image_to_base64(image_path: str) -> str:
    """Rasmni base64 formatga o‘tkazadi"""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")
    
    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode("utf-8")
    return encoded_string


def search_face(image_path: str, api_url: str = "http://192.168.30.64:8082/search"):
    """Rasmni API ga yuboradi va javobni chiqaradi"""
    try:
        image_b64 = image_to_base64(image_path)
        payload = {"image_base64": image_b64}

        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(payload), headers=headers, timeout=30)

        if response.status_code == 200:
            print("✅ Response received:")
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        else:
            print(f"❌ Error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"⚠️ Exception: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python client.py <image_path> [api_url]")
        sys.exit(1)

    image_path = sys.argv[1]
    api_url = sys.argv[2] if len(sys.argv) > 2 else "http://192.168.30.64:8082/search"
    search_face(image_path, api_url)
