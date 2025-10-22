# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1l1l1l1_opy_ import bstack11ll1ll11ll_opy_
from bstack_utils.constants import *
import json
class bstack111l1111l_opy_:
    def __init__(self, bstack1111ll1lll_opy_, bstack11ll11l1lll_opy_):
        self.bstack1111ll1lll_opy_ = bstack1111ll1lll_opy_
        self.bstack11ll11l1lll_opy_ = bstack11ll11l1lll_opy_
        self.bstack11ll11ll111_opy_ = None
    def __call__(self):
        bstack11ll11l1ll1_opy_ = {}
        while True:
            self.bstack11ll11ll111_opy_ = bstack11ll11l1ll1_opy_.get(
                bstack1l111ll_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᚾ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11l11ll_opy_ = self.bstack11ll11ll111_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11l11ll_opy_ > 0:
                sleep(bstack11ll11l11ll_opy_ / 1000)
            params = {
                bstack1l111ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᚿ"): self.bstack1111ll1lll_opy_,
                bstack1l111ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᛀ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack1l111ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᛁ") + bstack11ll11l1l11_opy_ + bstack1l111ll_opy_ (u"ࠤ࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡧࡰࡪ࠱ࡹ࠵࠴ࠨᛂ")
            if self.bstack11ll11l1lll_opy_.lower() == bstack1l111ll_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡶࠦᛃ"):
                bstack11ll11l1ll1_opy_ = bstack11ll1ll11ll_opy_.results(base_url, params)
            else:
                bstack11ll11l1ll1_opy_ = bstack11ll1ll11ll_opy_.bstack11ll11l1l1l_opy_(base_url, params)
            if str(bstack11ll11l1ll1_opy_.get(bstack1l111ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᛄ"), bstack1l111ll_opy_ (u"ࠬ࠸࠰࠱ࠩᛅ"))) != bstack1l111ll_opy_ (u"࠭࠴࠱࠶ࠪᛆ"):
                break
        return bstack11ll11l1ll1_opy_.get(bstack1l111ll_opy_ (u"ࠧࡥࡣࡷࡥࠬᛇ"), bstack11ll11l1ll1_opy_)