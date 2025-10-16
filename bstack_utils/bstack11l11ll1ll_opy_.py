# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11lll11l111_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import *
import json
class bstack11l111l111_opy_:
    def __init__(self, bstack11ll1l1lll_opy_, bstack11ll1l1111l_opy_):
        self.bstack11ll1l1lll_opy_ = bstack11ll1l1lll_opy_
        self.bstack11ll1l1111l_opy_ = bstack11ll1l1111l_opy_
        self.bstack11ll1l111l1_opy_ = None
    def __call__(self):
        bstack11ll1l111ll_opy_ = {}
        while True:
            self.bstack11ll1l111l1_opy_ = bstack11ll1l111ll_opy_.get(
                bstack1lllll1_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᚡ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll1l11l11_opy_ = self.bstack11ll1l111l1_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll1l11l11_opy_ > 0:
                sleep(bstack11ll1l11l11_opy_ / 1000)
            params = {
                bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚢ"): self.bstack11ll1l1lll_opy_,
                bstack1lllll1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᚣ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack1lllll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤᚤ") + bstack11ll1l11111_opy_ + bstack1lllll1_opy_ (u"ࠣ࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࠧᚥ")
            if self.bstack11ll1l1111l_opy_.lower() == bstack1lllll1_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡵࠥᚦ"):
                bstack11ll1l111ll_opy_ = bstack11lll111111_opy_.results(base_url, params)
            else:
                bstack11ll1l111ll_opy_ = bstack11lll111111_opy_.bstack11ll1l11l1l_opy_(base_url, params)
            if str(bstack11ll1l111ll_opy_.get(bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᚧ"), bstack1lllll1_opy_ (u"ࠫ࠷࠶࠰ࠨᚨ"))) != bstack1lllll1_opy_ (u"ࠬ࠺࠰࠵ࠩᚩ"):
                break
        return bstack11ll1l111ll_opy_.get(bstack1lllll1_opy_ (u"࠭ࡤࡢࡶࡤࠫᚪ"), bstack11ll1l111ll_opy_)