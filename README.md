# Nano Banana 3 API watchlist and examples

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square)](https://muapi.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

Nano Banana 3 is an **unconfirmed successor name**. Google has not announced this model, and MuAPI has not announced an integration, endpoint, schema, or price. This repository tracks the possibility without presenting speculation as availability. Its runnable example targets the currently available Nano Banana Pro endpoint; it is not a Nano Banana 3 call.

## Related Projects

- [Nano Banana 3 API watch page on MuAPI](https://muapi.ai/nano-banana-3) — status and confirmed updates.
- [Nano Banana API on MuAPI](https://muapi.ai/nano-banana-api) — current live family.
- [MuAPI API reference](https://muapi.ai/docs/api-reference) and [API keys](https://muapi.ai/access-keys).
- [GPT Image 3 API watchlist](https://github.com/Anil-matcha/GPT-Image-3-API) — related speculative image-model tracker.
- [Awesome AI Image Models](https://github.com/Anil-matcha/awesome-ai-image-models) — image model and API comparisons.
- [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) — open model workflows and integrations.

## Use a live Nano Banana model today

Install the example dependency and set `MUAPI_API_KEY`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export MUAPI_API_KEY="your_muapi_api_key"
python examples/generate_current.py
```

The example calls `POST /api/v1/nano-banana-pro` with the documented `prompt`, `aspect_ratio`, and `resolution` fields, then polls `GET /api/v1/predictions/{request_id}/result`. Check the live [Nano Banana API page](https://muapi.ai/nano-banana-api) for current schema and pricing.

## Nano Banana 3 status

There is no confirmed launch date, API contract, pricing, or MuAPI availability for Nano Banana 3. Do not use this repository name as evidence of an announcement. If the model and integration are confirmed, this README will be updated with verified request fields, examples, limits, and pricing.

## License

MIT. See [LICENSE](LICENSE).
