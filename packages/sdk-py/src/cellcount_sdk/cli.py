import sys
import json
from . import blocks  # noqa: F401
from .runner import run_pipeline

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: -m cellcount_sdk <pipeline.yaml>"}), file=sys.stderr)
        sys.exit(1)
    df = run_pipeline(sys.argv[1])
    print(json.dumps({
        "columns": df.columns,
        "rows": df.rows(),
        "shape": list(df.shape)
    }))