## William Nauroy
## August 22, 2023

"""
Tests for downloading NAM model
"""

from datetime import datetime, timedelta

from herbie import Herbie, FastHerbie

today = datetime.utcnow().replace(
    hour=0, minute=0, second=0, microsecond=0
) - timedelta(days=1)

save_dir = "/tmp/Herbie-Tests/"


def test_nam():
    H = Herbie(
        today,
        priority="aws",
        product="awip12",
        model="nam",
        save_dir=save_dir,
    )

    assert H.grib, "NAM grib2 file not found"
    assert H.idx, "NAM index file not found"

    H.download(":PRMSL:")
    assert H.get_localFilePath(":PRMSL:").exists()

    H.xarray(":PRMSL:", remove_grib=False)
    assert H.get_localFilePath(":PRMSL:").exists()


def test_nam_ftpprd():
    H = Herbie(
        today,
        priority="ftpprd",
        product="awip12",
        model="nam",
        save_dir=save_dir,
    )

    assert H.grib, "NAM grib2 file not found"
    assert H.idx, "NAM index file not found"

    H.download(":PRMSL:")
    assert H.get_localFilePath(":PRMSL:").exists()

    H.xarray(":PRMSL:", remove_grib=False)
    assert H.get_localFilePath(":PRMSL:").exists()


def test_nam_fastherbie():
    FH = FastHerbie(
        [today],
        priority="aws",
        product="awip12",
        model="nam",
        save_dir=save_dir,
    )

    assert FH.file_exists, "GEFS grib2 file not found"
