"""Five Seconds to Explain the Glass.

Copies the pre-written one-sentence cat excuse into the output
directory exactly as written. The text is fixed: the grader runs
this program in a sandbox with no network, so it must not fetch,
render, or generate anything at run time.
"""

import os
import shutil


def main():
    # The excuse is settled before this program ever runs: a cat's
    # defence only works if it is spoken, not drafted on the spot.
    # Copying it verbatim keeps the wording — and the nerve — intact.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
