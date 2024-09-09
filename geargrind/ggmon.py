import os
import clipboard_monitor
from pathlib import Path
import time

OUT_PATH = Path.cwd() / "items"
FILE_SUFFIX = ".item"

class Context:
    def __init__(self, top):
        self.top = top
        top.mkdir(parents=True, exist_ok=True)
        self.find_last_item(top)
        print(f"{self.last_item=}")

    def inspect_item_text(self, text):
        if text.startswith("Item Class: "):
            text = text.replace("\r\n", "\n")
            if text != self.last_item:
                now = time.time_ns()
                filename = OUT_PATH / Path(f"{now}{FILE_SUFFIX}")
                print(filename)
                filename.write_text(text)
                self.last_path = filename
                self.last_item = text

    def find_last_item(self, dir):
        for root, dirs, files in os.walk(dir):
            dirs.clear()
            files = [p for p in [root / Path(f) for f in files] if p.suffix == FILE_SUFFIX]
            if len(files):
                p = max(files, key=lambda p: float(p.stem))
                self.last_path = p
                self.last_item = p.read_text()
            else:
                self.last_path = None
                self.last_item = None
        

def main():
    ctx = Context(OUT_PATH)

    clipboard_monitor.on_text(ctx.inspect_item_text)
    clipboard_monitor.wait()

if __name__ == "__main__":
    main()