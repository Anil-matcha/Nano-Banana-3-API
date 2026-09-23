# Nano Banana 3 API — Python Client and Image Generation Examples

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square)](https://muapi.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

Generate and edit images with the Nano Banana API through MuAPI. This repository includes a small Python client, runnable text-to-image and image-edit examples, and copy-paste cURL requests. MuAPI uses an asynchronous submit-and-poll workflow, so generation jobs return a request ID before the image is ready.

The examples below use the Nano Banana Pro routes currently documented in the MuAPI catalog.

## Related Projects

- [Nano Banana 3 API on MuAPI](https://muapi.ai/nano-banana-3)
- [Nano Banana API](https://muapi.ai/nano-banana-api) — live family models, API details, and pricing.
- [MuAPI API reference](https://muapi.ai/docs/api-reference)
- [MuAPI API keys](https://muapi.ai/access-keys)
- [GPT Image 3 API](https://github.com/Anil-matcha/GPT-Image-3-API) — related image generation and editing examples.
- [Awesome AI Image Models](https://github.com/Anil-matcha/awesome-ai-image-models) — compare image models and API providers.
- [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) — generative-media tools and workflows.

## Features

- Nano Banana Pro text-to-image generation.
- Nano Banana Pro Edit instruction-based image editing.
- Aspect-ratio and 1K, 2K, or 4K resolution options.
- A reusable Python client with task polling and error handling.
- Equivalent cURL requests for direct REST API use.

## Installation

```bash
git clone https://github.com/Anil-matcha/Nano-Banana-3-API.git
cd Nano-Banana-3-API
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export MUAPI_API_KEY="your_muapi_api_key"
```

The examples require Python 3.9+ and `requests`. You can also copy `.env.example` to `.env` and load it with your preferred environment-variable tool.

## Text-to-image

Run the included example:

```bash
python -m examples.generate
```

Or call the client from your own script:

```python
from nano_banana_api import NanoBananaAPI

api = NanoBananaAPI()  # Reads MUAPI_API_KEY from the environment
job = api.generate(
    prompt="A tiny glass greenhouse on a mossy forest floor, morning light",
    aspect_ratio="1:1",
    resolution="2k",
)

result = api.wait_for_completion(job["request_id"])
print(result)
```

The result JSON includes the completed task status and generated image output URL.

## Image editing

Nano Banana Pro Edit takes an instruction and one or more publicly accessible source-image URLs. The endpoint accepts up to eight images.

To run the included edit example, set a public input image URL:

```bash
export MUAPI_INPUT_IMAGE_URL="https://example.com/source.jpg"
python -m examples.edit
```

```python
from nano_banana_api import NanoBananaAPI

api = NanoBananaAPI()
job = api.edit(
    prompt="Keep the subject and composition; change the lighting to warm sunset",
    images_list=["https://example.com/source.jpg"],
    aspect_ratio="16:9",
    resolution="2k",
)
result = api.wait_for_completion(job["request_id"])
print(result)
```

For local files, first upload the image using MuAPI's [file upload endpoint](https://muapi.ai/docs/api-reference), then pass the returned URL in `images_list`.

## cURL

Text-to-image:

```bash
curl -X POST "https://api.muapi.ai/api/v1/nano-banana-pro" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A tiny glass greenhouse on a mossy forest floor, morning light",
    "aspect_ratio": "1:1",
    "resolution": "1k"
  }'
```

Image edit:

```bash
curl -X POST "https://api.muapi.ai/api/v1/nano-banana-pro-edit" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Keep the subject and composition; change the lighting to warm sunset",
    "images_list": ["https://example.com/source.jpg"],
    "aspect_ratio": "16:9",
    "resolution": "2k"
  }'
```

Both calls return a `request_id`. Poll the task result endpoint until its status is `completed` or `failed`:

```bash
curl "https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result" \
  -H "x-api-key: ${MUAPI_API_KEY}"
```

## API reference

Base URL: `https://api.muapi.ai/api/v1`

| Workflow | Method and route | Required fields |
| --- | --- | --- |
| Text-to-image | `POST /nano-banana-pro` | `prompt` |
| Image editing | `POST /nano-banana-pro-edit` | `prompt`, `images_list` |
| Poll for result | `GET /predictions/{request_id}/result` | Path parameter `request_id` |

All requests use the `x-api-key` header. Submit endpoints accept JSON and return a request ID for polling.

### Request parameters

| Field | Generation | Editing | Values and limits |
| --- | --- | --- | --- |
| `prompt` | Required | Required | Text instruction describing the desired image |
| `images_list` | — | Required | Array of 1–8 publicly accessible image URLs |
| `aspect_ratio` | Optional | Optional | `1:1`, `3:4`, `4:3`, `9:16`, `16:9`, `3:2`, `2:3`, `5:4`, `4:5`, `21:9`; default `1:1` |
| `resolution` | Optional | Optional | `1k`, `2k`, `4k`; default `1k` |

See the [Nano Banana API page](https://muapi.ai/nano-banana-api) for the current route availability and pricing.

## Asynchronous workflow

1. Submit a generation or edit request with your API key.
2. Save the returned `request_id`.
3. Poll `/api/v1/predictions/{request_id}/result`, or use the Python client's `wait_for_completion` helper.
4. On `completed`, read the generated image URL from the response. On `failed`, inspect the returned error details.

For production workloads, poll from a background worker or use MuAPI webhooks where available instead of holding a web request open.

## Errors and practical notes

- `requests.raise_for_status()` raises an HTTP error for rejected submissions or polling requests.
- A completed HTTP request only means the task was accepted; continue polling until the task reaches a terminal status.
- Source image URLs must be reachable by MuAPI. Upload local images first.
- Keep `MUAPI_API_KEY` in an environment variable or secret store; do not commit credentials.
- Confirm current endpoint availability, accepted values, and pricing on the live [Nano Banana API page](https://muapi.ai/nano-banana-api).

## License

MIT. See [LICENSE](LICENSE).
