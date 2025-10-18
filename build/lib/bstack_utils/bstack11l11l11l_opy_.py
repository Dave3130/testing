# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll11ll_opy_ import bstack11ll1l1l111_opy_
from bstack_utils.constants import *
import json
class bstack1l111llll_opy_:
    def __init__(self, bstack1l11lllll_opy_, bstack11ll11ll111_opy_):
        self.bstack1l11lllll_opy_ = bstack1l11lllll_opy_
        self.bstack11ll11ll111_opy_ = bstack11ll11ll111_opy_
        self.bstack11ll11l1ll1_opy_ = None
    def __call__(self):
        bstack11ll11ll11l_opy_ = {}
        while True:
            self.bstack11ll11l1ll1_opy_ = bstack11ll11ll11l_opy_.get(
                bstack11ll_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛅ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11l1l11_opy_ = self.bstack11ll11l1ll1_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11l1l11_opy_ > 0:
                sleep(bstack11ll11l1l11_opy_ / 1000)
            params = {
                bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᛆ"): self.bstack1l11lllll_opy_,
                bstack11ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᛇ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᛈ") + bstack11ll11l1l1l_opy_ + bstack11ll_opy_ (u"ࠤ࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡧࡰࡪ࠱ࡹ࠵࠴ࠨᛉ")
            if self.bstack11ll11ll111_opy_.lower() == bstack11ll_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡶࠦᛊ"):
                bstack11ll11ll11l_opy_ = bstack11ll1l1l111_opy_.results(base_url, params)
            else:
                bstack11ll11ll11l_opy_ = bstack11ll1l1l111_opy_.bstack11ll11l1lll_opy_(base_url, params)
            if str(bstack11ll11ll11l_opy_.get(bstack11ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᛋ"), bstack11ll_opy_ (u"ࠬ࠸࠰࠱ࠩᛌ"))) != bstack11ll_opy_ (u"࠭࠴࠱࠶ࠪᛍ"):
                break
        return bstack11ll11ll11l_opy_.get(bstack11ll_opy_ (u"ࠧࡥࡣࡷࡥࠬᛎ"), bstack11ll11ll11l_opy_)