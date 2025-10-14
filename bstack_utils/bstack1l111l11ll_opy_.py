# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11lll111l1l_opy_ import bstack11ll1lllll1_opy_
from bstack_utils.constants import *
import json
class bstack1lll1l11l1_opy_:
    def __init__(self, bstack1111l1lll1_opy_, bstack11ll11llll1_opy_):
        self.bstack1111l1lll1_opy_ = bstack1111l1lll1_opy_
        self.bstack11ll11llll1_opy_ = bstack11ll11llll1_opy_
        self.bstack11ll1l111ll_opy_ = None
    def __call__(self):
        bstack11ll1l11111_opy_ = {}
        while True:
            self.bstack11ll1l111ll_opy_ = bstack11ll1l11111_opy_.get(
                bstack11l1l11_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᚙ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11lllll_opy_ = self.bstack11ll1l111ll_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11lllll_opy_ > 0:
                sleep(bstack11ll11lllll_opy_ / 1000)
            params = {
                bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᚚ"): self.bstack1111l1lll1_opy_,
                bstack11l1l11_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ᚛"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11l1l11_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ᚜") + bstack11ll1l111l1_opy_ + bstack11l1l11_opy_ (u"ࠢ࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࠦ᚝")
            if self.bstack11ll11llll1_opy_.lower() == bstack11l1l11_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡴࠤ᚞"):
                bstack11ll1l11111_opy_ = bstack11ll1lllll1_opy_.results(base_url, params)
            else:
                bstack11ll1l11111_opy_ = bstack11ll1lllll1_opy_.bstack11ll1l1111l_opy_(base_url, params)
            if str(bstack11ll1l11111_opy_.get(bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ᚟"), bstack11l1l11_opy_ (u"ࠪ࠶࠵࠶ࠧᚠ"))) != bstack11l1l11_opy_ (u"ࠫ࠹࠶࠴ࠨᚡ"):
                break
        return bstack11ll1l11111_opy_.get(bstack11l1l11_opy_ (u"ࠬࡪࡡࡵࡣࠪᚢ"), bstack11ll1l11111_opy_)