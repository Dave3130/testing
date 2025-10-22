# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll11l1_opy_ import bstack11ll1ll1ll1_opy_
from bstack_utils.constants import *
import json
class bstack1l11ll11l1_opy_:
    def __init__(self, bstack1l1111l1ll_opy_, bstack11ll11l1ll1_opy_):
        self.bstack1l1111l1ll_opy_ = bstack1l1111l1ll_opy_
        self.bstack11ll11l1ll1_opy_ = bstack11ll11l1ll1_opy_
        self.bstack11ll11ll111_opy_ = None
    def __call__(self):
        bstack11ll11l11ll_opy_ = {}
        while True:
            self.bstack11ll11ll111_opy_ = bstack11ll11l11ll_opy_.get(
                bstack11l1l11_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᚽ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11l1l11_opy_ = self.bstack11ll11ll111_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11l1l11_opy_ > 0:
                sleep(bstack11ll11l1l11_opy_ / 1000)
            params = {
                bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚾ"): self.bstack1l1111l1ll_opy_,
                bstack11l1l11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᚿ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11l1l11_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤᛀ") + bstack11ll11l1l1l_opy_ + bstack11l1l11_opy_ (u"ࠣ࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࠧᛁ")
            if self.bstack11ll11l1ll1_opy_.lower() == bstack11l1l11_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡵࠥᛂ"):
                bstack11ll11l11ll_opy_ = bstack11ll1ll1ll1_opy_.results(base_url, params)
            else:
                bstack11ll11l11ll_opy_ = bstack11ll1ll1ll1_opy_.bstack11ll11l1lll_opy_(base_url, params)
            if str(bstack11ll11l11ll_opy_.get(bstack11l1l11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛃ"), bstack11l1l11_opy_ (u"ࠫ࠷࠶࠰ࠨᛄ"))) != bstack11l1l11_opy_ (u"ࠬ࠺࠰࠵ࠩᛅ"):
                break
        return bstack11ll11l11ll_opy_.get(bstack11l1l11_opy_ (u"࠭ࡤࡢࡶࡤࠫᛆ"), bstack11ll11l11ll_opy_)