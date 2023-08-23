## Brian Blaylock
## February 9, 2022
## Updated by William Nauroy
## August 23, 2023

"""
Tests for downloading GFS model
"""

from herbie import Herbie, FastHerbie

save_dir = "$TMPDIR/Herbie-Tests/"


def test_gefs():
    H = Herbie(
        "2023-01-01 06:00",
        model="gefs",
        fxx=12,
        member="mean",
        save_dir=save_dir,
    )

    assert H.grib, "GEFS grib2 file not found"
    assert H.idx, "GEFS index file not found"


def test_gefs_reforecast():
    H = Herbie(
        "2017-03-14",
        model="gefs_reforecast",
        fxx=12,
        member=0,
        variable_level="tmp_2m",
        save_dir=save_dir,
    )

    assert H.grib, "GEFS grib2 file not found"
    assert H.idx, "GEFS index file not found"


def test_gefs_fastherbie_multi_member():
    members = ["p01","p02"]
    FH = FastHerbie(
        ["2023-08-23"],
        model="gefs",
        fxx=[12],
        members=members,
        variable_level="tmp_2m",
        save_dir=save_dir,
    )

    assert len(FH.file_exists)==2, "GEFS grib2 file not found"
    assert FH.file_exists[0].member in members, "GEFS member not found"
    assert FH.file_exists[1].member in members, "GEFS member not found"


def test_gefs_fastherbie_one_member():
    FH = FastHerbie(
        ["2023-08-23"],
        model="gefs",
        fxx=[12],
        member='p01',
        variable_level="tmp_2m",
        save_dir=save_dir,
    )

    assert len(FH.file_exists)==1, "GEFS grib2 file not found"
    assert FH.file_exists[0].member in "p01", "GEFS member not found"
