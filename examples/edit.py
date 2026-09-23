"""Edit an image with Nano Banana Pro Edit."""

import os

from nano_banana_api import NanoBananaAPI


def main():
    image_url = os.environ["MUAPI_INPUT_IMAGE_URL"]
    api = NanoBananaAPI()
    job = api.edit(
        prompt="Keep the subject and composition; change the lighting to warm sunset",
        images_list=[image_url],
        resolution="2k",
    )
    print(api.wait_for_completion(job["request_id"]))


if __name__ == "__main__":
    main()
