# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll1l1l_opy_ import bstack11ll1ll11ll_opy_
from bstack_utils.constants import *
import json
class bstack111l1lllll_opy_:
    def __init__(self, bstack1111ll111_opy_, bstack11ll11l11l1_opy_):
        self.bstack1111ll111_opy_ = bstack1111ll111_opy_
        self.bstack11ll11l11l1_opy_ = bstack11ll11l11l1_opy_
        self.bstack11ll11l111l_opy_ = None
    def __call__(self):
        bstack11ll11l1111_opy_ = {}
        while True:
            self.bstack11ll11l111l_opy_ = bstack11ll11l1111_opy_.get(
                bstack1lll11l_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛅ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11l11ll_opy_ = self.bstack11ll11l111l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11l11ll_opy_ > 0:
                sleep(bstack11ll11l11ll_opy_ / 1000)
            params = {
                bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᛆ"): self.bstack1111ll111_opy_,
                bstack1lll11l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᛇ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack1lll11l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᛈ") + bstack11ll11l1l11_opy_ + bstack1lll11l_opy_ (u"ࠤ࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡧࡰࡪ࠱ࡹ࠵࠴ࠨᛉ")
            if self.bstack11ll11l11l1_opy_.lower() == bstack1lll11l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡶࠦᛊ"):
                bstack11ll11l1111_opy_ = bstack11ll1ll11ll_opy_.results(base_url, params)
            else:
                bstack11ll11l1111_opy_ = bstack11ll1ll11ll_opy_.bstack11ll11l1l1l_opy_(base_url, params)
            if str(bstack11ll11l1111_opy_.get(bstack1lll11l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᛋ"), bstack1lll11l_opy_ (u"ࠬ࠸࠰࠱ࠩᛌ"))) != bstack1lll11l_opy_ (u"࠭࠴࠱࠶ࠪᛍ"):
                break
        return bstack11ll11l1111_opy_.get(bstack1lll11l_opy_ (u"ࠧࡥࡣࡷࡥࠬᛎ"), bstack11ll11l1111_opy_)