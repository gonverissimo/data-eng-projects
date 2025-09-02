import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter

def method_kde(df, ax, width, height, **kwargs):
    # Direct KDE method for heatmap visualization
    sns.kdeplot(
        x=df["x"], y=df["y"],
        fill=True, thresh=0.03, levels=100,
        bw_method="scott",
        ax=ax, **kwargs
    )

def method_hist_gaussian(df, ax, width, height, bins=200, sigma=3, cmap=None, alpha=0.6):
    # Histogram + Gaussian filter method for large datasets
    x = df["x"].values
    y = df["y"].values
    bins_x = bins
    bins_y = max(10, int(bins * height / width))
    H, xedges, yedges = np.histogram2d(y, x, bins=(bins_y, bins_x),
                                       range=[[0, height], [0, width]])
    H = gaussian_filter(H, sigma=sigma)
    extent = [0, width, 0, height]
    # Display the heatmap
    ax.imshow(H.T, extent=extent, origin='lower', alpha=alpha, cmap=cmap)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True, help="CSV file with columns x,y")
    p.add_argument("--width", type=int, required=True, help="Viewport width in pixels")
    p.add_argument("--height", type=int, required=True, help="Viewport height in pixels")
    p.add_argument("--output", default="heatmap.png", help="Output PNG file")
    p.add_argument("--overlay", help="Image file (screenshot) to overlay")
    p.add_argument("--method", choices=["kde","hist"], default="kde", help="Heatmap generation method")
    p.add_argument("--bins", type=int, default=200, help="Number of bins for hist method")
    p.add_argument("--sigma", type=float, default=3.0, help="Gaussian blur sigma (hist method)")
    args = p.parse_args()

    df = pd.read_csv(args.csv)
    if not {"x","y"}.issubset(df.columns):
        raise SystemExit("CSV must contain 'x' and 'y' columns (pixels).")

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, args.width)
    ax.set_ylim(0, args.height)

    # If overlay image is provided, load and draw underneath heatmap
    if args.overlay:
        img = Image.open(args.overlay)
        # Warn if dimensions don't match viewport
        if img.size != (args.width, args.height):
            print(f"Warning: overlay image size {img.size} does not match viewport {args.width}x{args.height}. Adjusting visualization.")
        ax.imshow(img, extent=[0, args.width, 0, args.height], origin='lower')

    # Draw heatmap using the selected method
    if args.method == "kde":
        method_kde(df, ax, args.width, args.height, cmap="jet", alpha=0.6)
    else:
        method_hist_gaussian(df, ax, args.width, args.height, bins=args.bins, sigma=args.sigma, cmap="jet", alpha=0.6)

    # Invert Y-axis to match screen coordinates (origin top-left)
    ax.invert_yaxis()
    ax.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(args.output, dpi=150, bbox_inches="tight", pad_inches=0)
    print(f"Heatmap saved as {args.output}")

if __name__ == "__main__":
    main()