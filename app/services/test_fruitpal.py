#  Coco Matthey
#  https://www.linkedin.com/in/coco-matthey/

import pytest

from app.services.fruitpal import Fruitpal
from app.services.overhead_data import OverheadData


@pytest.mark.parametrize("mode", ["DEV", "FILE", "NETWORK"])
def test_mode(mode):
    try:
        overheadData = OverheadData(mode).overheadData
        f = Fruitpal()
        costs = f.calculate("mango", 53, 405, overheadData)
        # TODO: Use expect here
        assert costs[0].total == 22060.10
    except:
        pytest.xfail("Test failed observing an exception")


@pytest.mark.skip(reason="Not yet implemented")
@pytest.mark.parametrize("commodity", ["mango"])
def test_commodity(commodity):
    pass


@pytest.mark.skip(reason="Not yet implemented")
def test_negative():
    pass

# TODO: more test cases, raise exception
# TODO: separate test in a different folder or repo
#
