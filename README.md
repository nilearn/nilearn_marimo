# Nilearn Marimo notebooks

The structure of this repository is mostly adapted from
the [marimo template repo](https://github.com/marimo-team/marimo-gh-pages-template).

## 🧪 Testing

To test the export process, run `scripts/build.py` from the root directory.

```bash
tox run -e build
```

This will export all notebooks in a folder called `_site/` in the root directory.
Then to serve the site, run:

```bash
python -m http.server -d _site
```

This will serve the site at `http://localhost:8000`.
