# Python Pong

I originally completed projects from Angela Yu's 100 Days of Code course across 2021–2023. After the original files were lost during a laptop change, this project was reconstructed in 2026 with substantial AI coding assistance. The Git history represents the reconstruction and first GitHub publication, not the original course timeline.

A two-player Turtle Pong game. The model handles paddle limits, wall and paddle bounces, increasing ball speed, and scoring separately from the graphical window.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Player one uses W/S and player two uses the arrow keys. Run model tests with `pytest`.
