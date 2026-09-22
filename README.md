![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# SCS Runoff Depth Calculator
 
*For hydrologists and stormwater engineers: enter curve number, total rainfall, and antecedent moisture condition to instantly compute direct runoff depth using the SCS method.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Hydrology
 
A simple, single-screen web tool that implements the SCS Curve Number (CN) runoff depth estimation method, widely used in hydrology and stormwater design.

Inputs:
1. Curve Number (CN) – integer slider from 30 to 100 (step 1), representing the runoff potential of the land cover and soil group.
2. Total Rainfall Depth (P) – float number input in inches (0 to 20, step 0.01).
3. Antecedent Moisture Condition (AMC) – dropdown with three options: 'AMC II (Average)', 'AMC I (Dry)', 'AMC III (Wet)'.

Core logic:
- If AMC is not 'AMC II', adjust the entered CN using the standard SCS conversion:
    - AMC I: CN_I = CN_II / (2.281 - 0.01281 × CN_II)
    - AMC III: CN_III = CN_II / (0.427 + 0.00573 × CN_II)
- Round adjusted CN to nearest integer.
- Compute potential maximum retention S (inches): S = (1000 / adjusted_CN) - 10
- Compute initial abstraction Ia = 0.2 × S
- If P <= Ia, runoff Q = 0; otherwise Q = (P - Ia)² / (P + 0.8×S)
- Convert Q from inches to mm (1 in = 25.4 mm).
- Compute runoff ratio (Q/P) as a percentage.

Outputs (displayed in text boxes):
- Adjusted Curve Number (value used after AMC correction)
- Potential maximum retention S (inches)
- Initial abstraction Ia (inches)
- Direct Runoff Q (inches and mm, formatted to 2 decimals)
- Runoff ratio (%)

UI layout (Gradio):
- Title: 'SCS Curve Number Runoff Calculator'
- Row 1: CN slider (left) and Rainfall number input (right)
- Row 2: AMC dropdown (centered)
- Row 3: 'Compute Runoff' button (center)
- Row 4: Output text boxes in two columns: left (adjusted CN, S, Ia), right (Q in inches, Q in mm, runoff ratio)
- All components use clear labels and units.

No AI/ML component; all logic is deterministic hydrologic calculation.
 
## Run it
 
```bash
docker build -t scs-runoff-depth-calculator .
docker run -p 7860:7860 scs-runoff-depth-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-22.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
