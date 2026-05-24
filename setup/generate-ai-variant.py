#!/usr/bin/env python3
"""
Generate Elvis pose variants for clock minutes using Replicate inpainting.
Usage: python3 setup/generate-ai-variant.py <minute>
Example: python3 setup/generate-ai-variant.py 39
"""

import sys
import os
import base64
import replicate
from PIL import Image, ImageDraw
import io
import urllib.request

def encode_image(img: Image.Image, fmt="PNG") -> str:
    buf = io.BytesIO()
    img.save(buf, format=fmt)
    return "data:image/" + fmt.lower() + ";base64," + base64.b64encode(buf.getvalue()).decode()

def make_arm_mask(size=394) -> Image.Image:
    """White mask over Elvis's left arm/hand area (fingertip at ~32,252)."""
    mask = Image.new("RGB", (size, size), "black")
    draw = ImageDraw.Draw(mask)
    # Cover the extended left arm from the elbow out to the fingertip
    draw.ellipse([0, 170, 180, 320], fill="white")
    # Extend toward fingertip
    draw.ellipse([0, 220, 80, 290], fill="white")
    return mask

def minute_to_prompt_direction(minute: int) -> str:
    """Describe arm/head direction based on clock minute position."""
    # Clock: 0 min = top, 15 = right, 30 = bottom, 45 = left
    # Minute 39-44 range: roughly lower-left to left
    directions = {
        39: "arm extended upward-left at a steep upward angle, reaching high toward the upper-left",
        40: "arm extended to the left and slightly upward, hand raised above shoulder height",
        41: "arm extended outward to the left at a slight upward angle, hand at shoulder height",
        42: "arm fully extended outward to the left, hand level with waist, leaning forward",  # base
        43: "arm extended to the lower-left, hand dipping below waist level",
        44: "arm angled downward-left, hand reaching toward the lower-left toward the crowd",
    }
    return directions.get(minute, directions[42])

def run(minute: int):
    src_path = "/workspaces/celebClock/imgs/42-elvispresley.jpg"
    out_dir  = "/workspaces/celebClock/imgs/temp"
    os.makedirs(out_dir, exist_ok=True)
    out_path = f"{out_dir}/{minute}-elvispresley-ai1.jpg"

    print(f"Loading source: {src_path}")
    src = Image.open(src_path).convert("RGB")

    print("Building mask...")
    mask = make_arm_mask(394)

    direction = minute_to_prompt_direction(minute)
    prompt = (
        f"Vintage black and white concert photograph of Elvis Presley performing on stage, "
        f"{direction}, leaning forward dynamically, crowd in background, "
        f"1950s rock and roll performance, high contrast B&W photography, photorealistic"
    )
    negative = "color, modern, cartoon, painting, blurry, distorted face, extra limbs"

    print(f"Minute {minute} direction: {direction}")
    print("Sending to Replicate (stability-ai/stable-diffusion-inpainting)...")

    output = replicate.run(
        "stability-ai/stable-diffusion-inpainting:95b7223104132402a9ae91cc677285bc5eb997834bd2349fa486f53910fd68b3",
        input={
            "image":          encode_image(src),
            "mask":           encode_image(mask),
            "prompt":         prompt,
            "negative_prompt": negative,
            "num_inference_steps": 50,
            "guidance_scale": 7.5,
            "num_outputs": 1,
        }
    )

    url = output[0] if isinstance(output, list) else str(output)
    print(f"Result URL: {url}")

    print(f"Downloading to {out_path}...")
    urllib.request.urlretrieve(url, out_path)
    print(f"Saved: {out_path}")
    print("Done!")

if __name__ == "__main__":
    minute = int(sys.argv[1]) if len(sys.argv) > 1 else 39
    run(minute)
