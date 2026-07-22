#!/usr/bin/env python3
"""Generate the profile hero and Dormice artwork through an OpenAI-compatible API.

Set IMAGE_API_KEY in the environment before running. The key is intentionally never
stored in this repository.
"""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API_BASE = os.environ.get("IMAGE_API_BASE", "https://api.cornna.xyz").rstrip("/")
MODEL = os.environ.get("IMAGE_MODEL", "gpt-image-2")
API_KEY = os.environ.get("IMAGE_API_KEY")

PROMPTS = {
    ROOT / "assets" / "hero-v3.png": """Create one horizontal 3:2 fine-art oil painting for a GitHub developer profile masthead. Preserve the identity of a luminous blue-and-gold Impressionist water-lily garden, but make it more original, cinematic, and museum-worthy than a generic Monet imitation. Composition: an immersive twilight pond viewed at water level, a monumental cropped weeping willow anchoring the left edge, bold lily pads entering from the foreground, five tiny golden light-motes moving in a subtle constellation across the water, and one continuous fine ochre thread beginning at a small brass spool near the lower-left shore, flowing in a graceful irregular S-curve across the pond, then rising toward a pale dawn aperture in the upper-right sky. The thread symbolizes directing collaborating AI agents; it must remain poetic, never look like a circuit diagram. Reflections fragment into cobalt and cerulean brushstrokes that only faintly suggest structured notation, with no literal code. Asymmetrical composition, darkest visual weight at left, atmospheric release at right, deep cobalt #1E40AF, cerulean #2563EB, sky blue #60A5FA, pale blue #DBEAFE, canvas white #F8FAFC, and restrained ochre-gold #FBBF24. Thick impasto, dry-brush scumbling, broken color, wet mist, imperfect hand-painted contours, photographed museum-painting materiality. Gold occupies under ten percent. Leave a calm but richly painted central-lower band for later typography. ABSOLUTELY NO text, letters, logos, borders, frames, UI, screens, robots, faces, watermarks, signatures, or photorealism.""",
    ROOT / "assets" / "projects" / "dormice.png": """Create one horizontal 3:2 fine-art oil painting for a GitHub portfolio project card, in the exact same refined blue-and-gold Impressionist gallery family as a luminous water-lily series. Subject: Dormice, “the SQLite of agent sandboxes,” expressed poetically as a tiny warm dormouse sleeping safely inside one circular woven nest that is also an abstract sandbox. The nest floats on nocturnal cobalt water under a large pearl-blue moon. Around it, four concentric atmospheric states recede from warm gold to cold blue—active, frozen, stopped, archived—without labels. A single unbroken golden thread shaped like a key enters the nest, loops through four softly glowing chambers, and returns to the same dormouse, symbolizing idempotent acquire and persistent identity. The outermost chamber dissolves into a small distant cloud of mist, suggesting optional archive and restore. Include one quiet ledger-like stack of slate-blue tiles near the nest to suggest SQLite, but never paint a database icon or UI. The dormouse should be elegant and semi-naturalistic, curled asleep, not a cartoon mascot: warm ochre fur, delicate ears, long curled tail, gentle breathing implied by two tiny ripples. Ornate antique gold gallery frame fully visible around all edges, matching a curated exhibition. Cobalt #1E40AF, cerulean #2563EB, sky #60A5FA, pale #DBEAFE, canvas #F8FAFC, restrained ochre #FBBF24. Rich impasto and broken brushwork, luminous reflected moonlight, hand-painted contours, sophisticated museum-painting texture. ABSOLUTELY NO text, letters, labels, logos, code, UI, watermarks, signatures, neon cyberpunk, flat vectors, or childish cartoon style.""",
}


def request_image(prompt: str) -> bytes:
    if not API_KEY:
        raise SystemExit("IMAGE_API_KEY is required")
    payload = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "n": 1,
        "size": "1536x1024",
        "quality": "high",
        "output_format": "png",
        "response_format": "b64_json",
    }).encode()
    request = urllib.request.Request(
        f"{API_BASE}/v1/images/generations",
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            result = json.load(response)
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Image API returned HTTP {error.code}: {body}") from error

    item = result["data"][0]
    encoded = item.get("b64_json")
    if not encoded:
        raise RuntimeError("Image API returned no inline image payload")
    return base64.b64decode(encoded, validate=True)


def main() -> None:
    for path, prompt in PROMPTS.items():
        print(f"Generating {path.relative_to(ROOT)} with {MODEL}…", flush=True)
        image = request_image(prompt)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(image)
        print(f"Wrote {path.relative_to(ROOT)} ({len(image):,} bytes)", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
