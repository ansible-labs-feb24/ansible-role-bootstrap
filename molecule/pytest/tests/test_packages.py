import pytest
# Confirm that specific packages and versions are installed
@pytest.mark.parametrize("name,version", [
    ("python3-psutil", "5"),
    ("python3-cryptography", "3.2"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)
