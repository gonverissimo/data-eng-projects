import numpy as np
import pandas as pd
import argparse
import time

def generate(n=500, width=1920, height=1080, out="clicks.csv"):
    np.random.seed(42)

    hotspots = [
        (int(width*0.2), int(height*0.3), 50),
        (int(width*0.7), int(height*0.4), 80),
        (int(width*0.5), int(height*0.8), 60)
    ]
    xs = []
    ys = []
    for _ in range(n):
        if np.random.rand() < 0.75:
            hx, hy, sigma = hotspots[np.random.randint(0, len(hotspots))]
            x = int(np.clip(np.random.normal(hx, sigma), 0, width-1))
            y = int(np.clip(np.random.normal(hy, sigma), 0, height-1))
        else:
            x = np.random.randint(0, width)
            y = np.random.randint(0, height)
        xs.append(x)
        ys.append(y)

    df = pd.DataFrame({
        "x": xs,
        "y": ys,
        "timestamp": [int(time.time() * 1000) for _ in range(n)]
    })
    df.to_csv(out, index=False)
    print(f"Gerado {n} cliques em {out} (w={width}, h={height})")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=500)
    p.add_argument("--width", type=int, default=1920)
    p.add_argument("--height", type=int, default=1080)
    p.add_argument("--out", type=str, default="clicks.csv")
    args = p.parse_args()
    generate(args.n, args.width, args.height, args.out)
