# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11lll1111ll_opy_ import bstack11ll1llllll_opy_
from bstack_utils.constants import *
import json
class bstack11ll11ll1l_opy_:
    def __init__(self, bstack11lll1lll1_opy_, bstack11ll1l111l1_opy_):
        self.bstack11lll1lll1_opy_ = bstack11lll1lll1_opy_
        self.bstack11ll1l111l1_opy_ = bstack11ll1l111l1_opy_
        self.bstack11ll1l1111l_opy_ = None
    def __call__(self):
        bstack11ll1l111ll_opy_ = {}
        while True:
            self.bstack11ll1l1111l_opy_ = bstack11ll1l111ll_opy_.get(
                bstack1ll11_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᚠ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll1l11l1l_opy_ = self.bstack11ll1l1111l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll1l11l1l_opy_ > 0:
                sleep(bstack11ll1l11l1l_opy_ / 1000)
            params = {
                bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᚡ"): self.bstack11lll1lll1_opy_,
                bstack1ll11_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᚢ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack1ll11_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣᚣ") + bstack11ll1l11111_opy_ + bstack1ll11_opy_ (u"ࠢ࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࠦᚤ")
            if self.bstack11ll1l111l1_opy_.lower() == bstack1ll11_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡴࠤᚥ"):
                bstack11ll1l111ll_opy_ = bstack11ll1llllll_opy_.results(base_url, params)
            else:
                bstack11ll1l111ll_opy_ = bstack11ll1llllll_opy_.bstack11ll1l11l11_opy_(base_url, params)
            if str(bstack11ll1l111ll_opy_.get(bstack1ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᚦ"), bstack1ll11_opy_ (u"ࠪ࠶࠵࠶ࠧᚧ"))) != bstack1ll11_opy_ (u"ࠫ࠹࠶࠴ࠨᚨ"):
                break
        return bstack11ll1l111ll_opy_.get(bstack1ll11_opy_ (u"ࠬࡪࡡࡵࡣࠪᚩ"), bstack11ll1l111ll_opy_)