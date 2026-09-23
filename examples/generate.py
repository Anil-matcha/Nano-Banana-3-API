"""Generate an image through MuAPI's Nano Banana endpoint."""

from nano_banana_api import NanoBananaAPI


def main():
    api = NanoBananaAPI()
    job = api.generate(
        prompt="A tiny glass greenhouse on a mossy forest floor, morning light",
        aspect_ratio="1:1",
        resolution="1k",
    )
    request_id = job["request_id"]
    print(f"Submitted request: {request_id}")
    print(api.wait_for_completion(request_id))


if __name__ == "__main__":
    main()
