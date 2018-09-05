import sphinxience
import tomlkit
from pathlib import Path

PYPROJECT_FILE = Path(__file__).parent.parent / 'pyproject.toml'

def test_versions_consistent():
    version_in_module = sphinxience.__version__

    pyproject_contents = open(PYPROJECT_FILE).read()
    parsed = tomlkit.parse(pyproject_contents)
    version_in_pyproject = parsed['tool']['poetry']['version']

    assert version_in_module == version_in_pyproject
