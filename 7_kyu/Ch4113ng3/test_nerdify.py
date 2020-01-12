from nerdify import nerdify


def test_nerdify():
    assert nerdify("Fundamentals") == "Fund4m3nt41s"
    assert nerdify("Seven") == "S3v3n"
    assert nerdify("Los Angeles") == "Los 4ng313s"
    assert nerdify("Seoijselawuue") == "S3oijs314wuu3"
