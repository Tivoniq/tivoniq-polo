#!/usr/bin/env python3
"""Fill the official TIVONIQ logo files into the viewer source.

    git clone https://github.com/Tivoniq/tivoniq-brand
    python3 src/build.py ../tivoniq-brand      # writes src/polo-3d.fragment.html

The published index.html is this fragment wrapped in a standard HTML document.
"""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
logo = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else here.parent.parent / "tivoniq-brand") / "logo" / "svg"
src = (here / "polo-3d.src.html").read_text()
src = src.replace("__WM_COLOR__", (logo / "tivoniq-wordmark-color.svg").read_text())
src = src.replace("__WM_WHITE__", (logo / "tivoniq-wordmark-white.svg").read_text())
src = src.replace("__MARK_WHITE__", json.dumps((logo / "tivoniq-mark-white.svg").read_text()))
src = src.replace("__MARK_NAVY__", json.dumps((logo / "tivoniq-mark-navy.svg").read_text()))
(here / "polo-3d.fragment.html").write_text(src)
print(here / "polo-3d.fragment.html")
