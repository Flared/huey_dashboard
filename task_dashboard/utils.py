from typing import Dict, Any


def extract_sub_config(config: Dict[str, Any], prefix: str) -> Dict[str, Any]:
    return {k[len(prefix) :]: v for k, v in config.items() if k.startswith(prefix)}
