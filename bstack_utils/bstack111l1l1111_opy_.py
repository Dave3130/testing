# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll11l1_opy_ import bstack11ll1ll1ll1_opy_
from bstack_utils.constants import *
import json
class bstack11l11l11l1_opy_:
    def __init__(self, bstack1lllll111l_opy_, bstack11ll11lllll_opy_):
        self.bstack1lllll111l_opy_ = bstack1lllll111l_opy_
        self.bstack11ll11lllll_opy_ = bstack11ll11lllll_opy_
        self.bstack11ll1l1111l_opy_ = None
    def __call__(self):
        bstack11ll1l111ll_opy_ = {}
        while True:
            self.bstack11ll1l1111l_opy_ = bstack11ll1l111ll_opy_.get(
                bstack1ll1l_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭᚛"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll1l111l1_opy_ = self.bstack11ll1l1111l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll1l111l1_opy_ > 0:
                sleep(bstack11ll1l111l1_opy_ / 1000)
            params = {
                bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᚜"): self.bstack1lllll111l_opy_,
                bstack1ll1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ᚝"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack1ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ᚞") + bstack11ll1l11111_opy_ + bstack1ll1l_opy_ (u"ࠤ࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡧࡰࡪ࠱ࡹ࠵࠴ࠨ᚟")
            if self.bstack11ll11lllll_opy_.lower() == bstack1ll1l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡶࠦᚠ"):
                bstack11ll1l111ll_opy_ = bstack11ll1ll1ll1_opy_.results(base_url, params)
            else:
                bstack11ll1l111ll_opy_ = bstack11ll1ll1ll1_opy_.bstack11ll11llll1_opy_(base_url, params)
            if str(bstack11ll1l111ll_opy_.get(bstack1ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᚡ"), bstack1ll1l_opy_ (u"ࠬ࠸࠰࠱ࠩᚢ"))) != bstack1ll1l_opy_ (u"࠭࠴࠱࠶ࠪᚣ"):
                break
        return bstack11ll1l111ll_opy_.get(bstack1ll1l_opy_ (u"ࠧࡥࡣࡷࡥࠬᚤ"), bstack11ll1l111ll_opy_)