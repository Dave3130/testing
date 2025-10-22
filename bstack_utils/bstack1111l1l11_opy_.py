# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll1lll_opy_ import bstack11ll1l1llll_opy_
from bstack_utils.constants import *
import json
class bstack11ll11ll1_opy_:
    def __init__(self, bstack11111l11l_opy_, bstack11ll11l1lll_opy_):
        self.bstack11111l11l_opy_ = bstack11111l11l_opy_
        self.bstack11ll11l1lll_opy_ = bstack11ll11l1lll_opy_
        self.bstack11ll11l1ll1_opy_ = None
    def __call__(self):
        bstack11ll11ll11l_opy_ = {}
        while True:
            self.bstack11ll11l1ll1_opy_ = bstack11ll11ll11l_opy_.get(
                bstack1lllll1l_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛁ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11ll1l1_opy_ = self.bstack11ll11l1ll1_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11ll1l1_opy_ > 0:
                sleep(bstack11ll11ll1l1_opy_ / 1000)
            params = {
                bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᛂ"): self.bstack11111l11l_opy_,
                bstack1lllll1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᛃ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack1lllll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᛄ") + bstack11ll11l1l1l_opy_ + bstack1lllll1l_opy_ (u"ࠧ࠵ࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࠤᛅ")
            if self.bstack11ll11l1lll_opy_.lower() == bstack1lllll1l_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࡹࠢᛆ"):
                bstack11ll11ll11l_opy_ = bstack11ll1l1llll_opy_.results(base_url, params)
            else:
                bstack11ll11ll11l_opy_ = bstack11ll1l1llll_opy_.bstack11ll11ll111_opy_(base_url, params)
            if str(bstack11ll11ll11l_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᛇ"), bstack1lllll1l_opy_ (u"ࠨ࠴࠳࠴ࠬᛈ"))) != bstack1lllll1l_opy_ (u"ࠩ࠷࠴࠹࠭ᛉ"):
                break
        return bstack11ll11ll11l_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡨࡦࡺࡡࠨᛊ"), bstack11ll11ll11l_opy_)