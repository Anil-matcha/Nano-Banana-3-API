"""Runnable Nano Banana Pro example; Nano Banana 3 is not yet confirmed."""

import os
import time

import requests


BASE_URL = "https://api.muapi.ai/api/v1"


def main():
    api_key = os.environ["MUAPI_API_KEY"]
    headers = {"x-api-key": api_key, "Content-Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}/nano-banana-pro",
        headers=headers,
        json={
            "prompt": "A tiny glass greenhouse on a mossy forest floor, morning light",
            "aspect_ratio": "1:1",
            "resolution": "1k",
        },
        timeout=60,
    )
    response.raise_for_status()
    request_id = response.json()["request_id"]
    print(f"Submitted request: {request_id}")

    while True:
        result = requests.get(
            f"{BASE_URL}/predictions/{request_id}/result",
            headers={"x-api-key": api_key},
            timeout=60,
        )
        result.raise_for_status()
        body = result.json()
        if body.get("status") == "completed":
            print(body)
            return
        if body.get("status") == "failed":
            raise RuntimeError(body)
        time.sleep(2)


if __name__ == "__main__":
    main()
