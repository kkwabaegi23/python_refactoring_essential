git add .
uv run --with requests python -m unittest discover && git commit -m "$1" || git reset --hard