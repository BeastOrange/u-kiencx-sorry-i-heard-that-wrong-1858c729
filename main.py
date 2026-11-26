import os
from pathlib import Path

ONE_LINE = "Sorry, I misheard 'order paper towels' as 'couples therapy.' Our first session is Thursday, and I have five years of audio to unpack."


def main():
    print(ONE_LINE)
    if os.path.isdir("/output"):
        out_path = Path("/output/entry.txt")
    else:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
    out_path.write_text(ONE_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
