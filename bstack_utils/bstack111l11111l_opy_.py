# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11lll111lll_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import *
import json
class bstack11l111l111_opy_:
    def __init__(self, bstack1111ll1l1_opy_, bstack11ll11llll1_opy_):
        self.bstack1111ll1l1_opy_ = bstack1111ll1l1_opy_
        self.bstack11ll11llll1_opy_ = bstack11ll11llll1_opy_
        self.bstack11ll11lll1l_opy_ = None
    def __call__(self):
        bstack11ll11lll11_opy_ = {}
        while True:
            self.bstack11ll11lll1l_opy_ = bstack11ll11lll11_opy_.get(
                bstack11l111_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᚐ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11lllll_opy_ = self.bstack11ll11lll1l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11lllll_opy_ > 0:
                sleep(bstack11ll11lllll_opy_ / 1000)
            params = {
                bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚑ"): self.bstack1111ll1l1_opy_,
                bstack11l111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᚒ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᚓ") + bstack11ll1l1111l_opy_ + bstack11l111_opy_ (u"ࠧ࠵ࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࠤᚔ")
            if self.bstack11ll11llll1_opy_.lower() == bstack11l111_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࡹࠢᚕ"):
                bstack11ll11lll11_opy_ = bstack11lll111111_opy_.results(base_url, params)
            else:
                bstack11ll11lll11_opy_ = bstack11lll111111_opy_.bstack11ll1l11111_opy_(base_url, params)
            if str(bstack11ll11lll11_opy_.get(bstack11l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᚖ"), bstack11l111_opy_ (u"ࠨ࠴࠳࠴ࠬᚗ"))) != bstack11l111_opy_ (u"ࠩ࠷࠴࠹࠭ᚘ"):
                break
        return bstack11ll11lll11_opy_.get(bstack11l111_opy_ (u"ࠪࡨࡦࡺࡡࠨᚙ"), bstack11ll11lll11_opy_)