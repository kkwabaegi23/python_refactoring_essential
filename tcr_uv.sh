git add .
uv run python -m unittest discover && git commit -m "$1" || git reset --hard