# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1l1ll1l_opy_ import bstack11ll1l1l11l_opy_
from bstack_utils.constants import *
import json
class bstack11l11ll11l_opy_:
    def __init__(self, bstack1ll111ll1_opy_, bstack11ll11ll1l1_opy_):
        self.bstack1ll111ll1_opy_ = bstack1ll111ll1_opy_
        self.bstack11ll11ll1l1_opy_ = bstack11ll11ll1l1_opy_
        self.bstack11ll11ll11l_opy_ = None
    def __call__(self):
        bstack11ll11ll111_opy_ = {}
        while True:
            self.bstack11ll11ll11l_opy_ = bstack11ll11ll111_opy_.get(
                bstack11l111_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛃ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11l1lll_opy_ = self.bstack11ll11ll11l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11l1lll_opy_ > 0:
                sleep(bstack11ll11l1lll_opy_ / 1000)
            params = {
                bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᛄ"): self.bstack1ll111ll1_opy_,
                bstack11l111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᛅ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣᛆ") + bstack11ll11l1ll1_opy_ + bstack11l111_opy_ (u"ࠢ࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࠦᛇ")
            if self.bstack11ll11ll1l1_opy_.lower() == bstack11l111_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡴࠤᛈ"):
                bstack11ll11ll111_opy_ = bstack11ll1l1l11l_opy_.results(base_url, params)
            else:
                bstack11ll11ll111_opy_ = bstack11ll1l1l11l_opy_.bstack11ll11l1l1l_opy_(base_url, params)
            if str(bstack11ll11ll111_opy_.get(bstack11l111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛉ"), bstack11l111_opy_ (u"ࠪ࠶࠵࠶ࠧᛊ"))) != bstack11l111_opy_ (u"ࠫ࠹࠶࠴ࠨᛋ"):
                break
        return bstack11ll11ll111_opy_.get(bstack11l111_opy_ (u"ࠬࡪࡡࡵࡣࠪᛌ"), bstack11ll11ll111_opy_)