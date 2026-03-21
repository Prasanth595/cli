import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    yaml = None


@dataclass
class BatchRequestItem:
    name: str
    method: str
    url: str
    headers: Optional[Dict[str, str]] = None
    params: Optional[Dict[str, Any]] = None
    json_body: Optional[Any] = None
    data: Optional[Any] = None
    auth: Optional[Dict[str, Any]] = None
    group: Optional[str] = None


@dataclass
class BatchExecutionResult:
    name: str
    method: str
    url: str
    success: bool
    status_code: Optional[int] = None
    error: Optional[str] = None
    response_text: Optional[str] = None


class BatchExecutor:
    def __init__(
        self,
        template_file: str,
        exec_mode: str = "all",
        preview: bool = False,
        output_dir: str = "batch_results",
        output_format: str = "json",
        verbose: bool = False,
    ) -> None:
        self.template_file = Path(template_file)
        self.exec_mode = exec_mode
        self.preview = preview
        self.output_dir = Path(output_dir)
        self.output_format = output_format
        self.verbose = verbose
        self.requests: List[BatchRequestItem] = []

    def load_templates(self) -> List[BatchRequestItem]:
        if not self.template_file.exists():
            raise FileNotFoundError(f"Template file not found: {self.template_file}")

        suffix = self.template_file.suffix.lower()
        content = self.template_file.read_text(encoding="utf-8")

        if suffix in [".yaml", ".yml"]:
            if yaml is None:
                raise RuntimeError("PyYAML is required for YAML batch templates")
            raw = yaml.safe_load(content)
        elif suffix == ".json":
            raw = json.loads(content)
        else:
            raise ValueError(f"Unsupported template format: {suffix}")

        items = raw.get("requests", raw if isinstance(raw, list) else [])
        self.requests = [BatchRequestItem(**item) for item in items]
        return self.requests

    def preview_requests(self) -> None:
        print("Batch request preview:")
        for idx, req in enumerate(self.requests, start=1):
            print(f"{idx}. [{req.method}] {req.name} -> {req.url}")

    def select_requests(self) -> List[BatchRequestItem]:
        if self.exec_mode == "all":
            return self.requests

        if self.exec_mode == "interactive":
            print("Interactive mode is not fully verified yet.")
            selected = []
            for req in self.requests:
                answer = input(f"Execute '{req.name}'? [y/N]: ").strip().lower()
                if answer == "y":
                    selected.append(req)
            return selected

        if self.exec_mode == "preview":
            return []

        raise ValueError(f"Unsupported exec mode: {self.exec_mode}")

    def execute_one(self, req: BatchRequestItem) -> BatchExecutionResult:
        """
        这里暂时只放占位逻辑。
        真正集成时，应接 HTTPie 现有请求执行流程，而不是自己重复造轮子。
        """
        try:
            # TODO: 替换为 HTTPie 核心请求执行调用
            if self.verbose:
                print(f"Executing: [{req.method}] {req.url}")

            return BatchExecutionResult(
                name=req.name,
                method=req.method,
                url=req.url,
                success=False,
                error="Execution path not integrated with HTTPie core yet",
            )
        except Exception as exc:
            return BatchExec
