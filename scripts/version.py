import dataclasses
import subprocess
from typing import Optional


@dataclasses.dataclass
class Version:
    major: int = 0
    minor: int = 0
    user: int = 0
    dirty: bool = False
    branch: Optional[str] = None

    def __str__(self):
        dirty = "m" if self.dirty else ""
        branch = ""
        if self.branch is not None:
            branch = f'({self.branch.replace("/", "_")})'
        return f"{self.major}.{self.minor}{'' if self.user == 0 else f'.{self.user}'}{dirty}{branch}"


def version_info():
    version = Version()

    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        if branch not in ("master", "main", "HEAD"):
            version.branch = branch
        info = subprocess.check_output(["git", "describe", "--tags", "--dirty", "--long", "--always"]).decode().strip().split('-')
        if info[-1] == "dirty":
            version.dirty = True
            info.pop()

        if len(info) >= 2:
            # drop abbrev
            info.pop()
            version.user = int(info.pop())
            text = info.pop(0)
            if text.startswith('v') or text.startswith('V'):
                text = text[1:]
            parts = text.split('.')
            version.major = int(parts[0])
            if len(parts) > 1:
                version.minor = int(parts[1])

        else:
            # no tag so far
            version.user = int(subprocess.check_output(["git", "rev-list", "--all", "--count"]).decode().strip())
    except Exception as e:
        version.major = -1

    return version


if __name__ == "__main__":
    print(version_info())