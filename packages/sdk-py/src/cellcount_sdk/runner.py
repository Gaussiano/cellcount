import hashlib
import json
import yaml
from pathlib import Path
import polars as pl
from .block import get_block

CACHE_DIR = Path(".cache")

def _hash(block_name: str, params: dict, input_hash: str | None) -> str:
    payload = json.dumps({"b": block_name, "p": params, "i": input_hash}, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()[:16]

def run_pipeline(path: str) -> pl.DataFrame:
    CACHE_DIR.mkdir(exist_ok=True)
    with open(path) as f:
        pipeline = yaml.safe_load(f)

    result = None
    prev_hash = None

    for step in pipeline["steps"]:
        spec = get_block(step["block"])
        params = step.get("params", {})
        step_hash = _hash(step["block"], params, prev_hash)
        cache_file = CACHE_DIR / f"{step_hash}.parquet"

        if cache_file.exists():
            print(f"[cache] {step['block']}", flush=True)
            result = pl.read_parquet(cache_file)
        else:
            print(f"[run]   {step['block']}", flush=True)
            result = spec.func(params=params, inputs={"prev": result})
            result.write_parquet(cache_file)

        prev_hash = step_hash

    return result