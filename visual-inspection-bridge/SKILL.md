---
name: visual-inspection-bridge
description: Analyze real screenshots/images using local LLaVA when native vision tools are unavailable
version: 1.0.0
category: vision
tags: [vision, llava, screenshots, verification]
---

## When to Use

Use only when an actual image file exists and must be visually inspected.

Examples:
- screenshots
- charts
- photos
- UI captures
- diagrams

Do not use for:
- missing notes
- blocked websites
- unavailable documents
- text recovery

## Procedure

1. Find or capture the image file.

2. Confirm the image file exists.

3. Execute:

python3 ~/kokoro/vision_analyze.py IMAGE_PATH

4. Wait for the LLaVA output.

5. Use only the returned visual analysis as evidence.

6. If the command fails:
- fix image path
- verify image format
- retry

Never claim to have visually inspected an image unless the LLaVA command succeeds.
