import re


def strip_command(msg: str | None) -> str | None:
    if not msg:
        return None
    match = re.search(r"(/\w+\s+)(.*)$", msg)
    return match.group(2) if match else None


def find_index_in_text(msg: str | None) -> int | None:
    if not msg:
        return None
    match = re.search(r"\#(\d+)", msg)
    return int(match.group(1)) if match else None
