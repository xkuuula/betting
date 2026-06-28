import sys
from pathlib import Path


def _add_project_path() -> None:
    app_dir = Path(__file__).resolve().parent
    candidates = [
        app_dir,
        app_dir / "src",
        *(
            package_dir.parent
            for package_dir in app_dir.rglob("polymarket_cs2_alerts")
            if package_dir.is_dir()
        ),
    ]

    for path in candidates:
        if (path / "polymarket_cs2_alerts" / "__init__.py").exists():
            sys.path.insert(0, str(path))
            return

    visible = ", ".join(sorted(item.name for item in app_dir.iterdir()))
    raise RuntimeError(
        "Cannot find polymarket_cs2_alerts package. "
        "Upload the whole project, not only server.py. "
        f"Files visible in /app: {visible}"
    )


_add_project_path()

from polymarket_cs2_alerts.main import main  # noqa: E402

if __name__ == "__main__":
    main()
