# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll1ll1_opy_ import bstack11ll1ll11ll_opy_
from bstack_utils.constants import *
import json
class bstack11lll1111_opy_:
    def __init__(self, bstack11l1lll1ll_opy_, bstack11ll11lllll_opy_):
        self.bstack11l1lll1ll_opy_ = bstack11l1lll1ll_opy_
        self.bstack11ll11lllll_opy_ = bstack11ll11lllll_opy_
        self.bstack11ll1l111l1_opy_ = None
    def __call__(self):
        bstack11ll11llll1_opy_ = {}
        while True:
            self.bstack11ll1l111l1_opy_ = bstack11ll11llll1_opy_.get(
                bstack11111_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᚐ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll1l11111_opy_ = self.bstack11ll1l111l1_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll1l11111_opy_ > 0:
                sleep(bstack11ll1l11111_opy_ / 1000)
            params = {
                bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚑ"): self.bstack11l1lll1ll_opy_,
                bstack11111_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᚒ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᚓ") + bstack11ll11lll1l_opy_ + bstack11111_opy_ (u"ࠧ࠵ࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࠤᚔ")
            if self.bstack11ll11lllll_opy_.lower() == bstack11111_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࡹࠢᚕ"):
                bstack11ll11llll1_opy_ = bstack11ll1ll11ll_opy_.results(base_url, params)
            else:
                bstack11ll11llll1_opy_ = bstack11ll1ll11ll_opy_.bstack11ll1l1111l_opy_(base_url, params)
            if str(bstack11ll11llll1_opy_.get(bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᚖ"), bstack11111_opy_ (u"ࠨ࠴࠳࠴ࠬᚗ"))) != bstack11111_opy_ (u"ࠩ࠷࠴࠹࠭ᚘ"):
                break
        return bstack11ll11llll1_opy_.get(bstack11111_opy_ (u"ࠪࡨࡦࡺࡡࠨᚙ"), bstack11ll11llll1_opy_)