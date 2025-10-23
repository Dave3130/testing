# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1lllll1_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import *
import json
class bstack1l11111ll_opy_:
    def __init__(self, bstack11lll1l1ll_opy_, bstack11ll1l1111l_opy_):
        self.bstack11lll1l1ll_opy_ = bstack11lll1l1ll_opy_
        self.bstack11ll1l1111l_opy_ = bstack11ll1l1111l_opy_
        self.bstack11ll1l111ll_opy_ = None
    def __call__(self):
        bstack11ll1l111l1_opy_ = {}
        while True:
            self.bstack11ll1l111ll_opy_ = bstack11ll1l111l1_opy_.get(
                bstack111111l_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᚖ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11lllll_opy_ = self.bstack11ll1l111ll_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11lllll_opy_ > 0:
                sleep(bstack11ll11lllll_opy_ / 1000)
            params = {
                bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᚗ"): self.bstack11lll1l1ll_opy_,
                bstack111111l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᚘ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack111111l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧᚙ") + bstack11ll11llll1_opy_ + bstack111111l_opy_ (u"ࠦ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࠣᚚ")
            if self.bstack11ll1l1111l_opy_.lower() == bstack111111l_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࡸࠨ᚛"):
                bstack11ll1l111l1_opy_ = bstack11lll111111_opy_.results(base_url, params)
            else:
                bstack11ll1l111l1_opy_ = bstack11lll111111_opy_.bstack11ll1l11111_opy_(base_url, params)
            if str(bstack11ll1l111l1_opy_.get(bstack111111l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭᚜"), bstack111111l_opy_ (u"ࠧ࠳࠲࠳ࠫ᚝"))) != bstack111111l_opy_ (u"ࠨ࠶࠳࠸ࠬ᚞"):
                break
        return bstack11ll1l111l1_opy_.get(bstack111111l_opy_ (u"ࠩࡧࡥࡹࡧࠧ᚟"), bstack11ll1l111l1_opy_)