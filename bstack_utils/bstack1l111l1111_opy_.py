# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1llllll_opy_ import bstack11ll1llll11_opy_
from bstack_utils.constants import *
import json
class bstack111111llll_opy_:
    def __init__(self, bstack11ll11lll1_opy_, bstack11ll11ll1l1_opy_):
        self.bstack11ll11lll1_opy_ = bstack11ll11lll1_opy_
        self.bstack11ll11ll1l1_opy_ = bstack11ll11ll1l1_opy_
        self.bstack11ll11ll11l_opy_ = None
    def __call__(self):
        bstack11ll11l1lll_opy_ = {}
        while True:
            self.bstack11ll11ll11l_opy_ = bstack11ll11l1lll_opy_.get(
                bstack11l11l1_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᚶ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11ll111_opy_ = self.bstack11ll11ll11l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11ll111_opy_ > 0:
                sleep(bstack11ll11ll111_opy_ / 1000)
            params = {
                bstack11l11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚷ"): self.bstack11ll11lll1_opy_,
                bstack11l11l1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᚸ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11l11l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤᚹ") + bstack11ll11lll11_opy_ + bstack11l11l1_opy_ (u"ࠣ࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࠧᚺ")
            if self.bstack11ll11ll1l1_opy_.lower() == bstack11l11l1_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡵࠥᚻ"):
                bstack11ll11l1lll_opy_ = bstack11ll1llll11_opy_.results(base_url, params)
            else:
                bstack11ll11l1lll_opy_ = bstack11ll1llll11_opy_.bstack11ll11ll1ll_opy_(base_url, params)
            if str(bstack11ll11l1lll_opy_.get(bstack11l11l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᚼ"), bstack11l11l1_opy_ (u"ࠫ࠷࠶࠰ࠨᚽ"))) != bstack11l11l1_opy_ (u"ࠬ࠺࠰࠵ࠩᚾ"):
                break
        return bstack11ll11l1lll_opy_.get(bstack11l11l1_opy_ (u"࠭ࡤࡢࡶࡤࠫᚿ"), bstack11ll11l1lll_opy_)