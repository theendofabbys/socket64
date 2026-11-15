import os
import sys
import shutil
import platform
import subprocess
from pathlib import Path

REPO = "https://github.com/qsocket/qsocket"
PROJECT = Path.home() / "qsocket"
PREFIX = os.environ.get("PREFIX")

ENV = os.environ.copy()
ENV["GOTOOLCHAIN"] = "local"


def run(cmd, cwd=None):
    subprocess.run(
        cmd,
        cwd=cwd,
        env=ENV,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )


def main():
    if not PREFIX or not shutil.which("pkg"):
        raise RuntimeError()

    if platform.machine().lower() not in ("aarch64", "arm64"):
        raise RuntimeError()

    if not shutil.which("git") or not shutil.which("go"):
        run(["pkg", "update"])
        run(["pkg", "install", "git", "golang", "-y"])

    if PROJECT.exists():
        if not (PROJECT / ".git").exists():
            raise RuntimeError()
    else:
        run(["git", "clone", REPO, str(PROJECT)])

    run(["go", "mod", "edit", "-go=1.26"], cwd=PROJECT)
    run(["go", "mod", "tidy"], cwd=PROJECT)

    run([
        "go", "build",
        "-trimpath",
        "-o", "qsock",
        "./cmd/qsock"
    ], cwd=PROJECT)

    binary = PROJECT / "qsock"
    destination = Path(PREFIX) / "bin" / "qsock"

    if not binary.is_file():
        raise RuntimeError()

    shutil.copy2(binary, destination)
    destination.chmod(0o755)

    run(["qsock", "--help"])


if __name__ == "__main__":
    try:
        main()
        print("sucesso")
    except BaseException:
        print("error")
        sys.exit(1)
