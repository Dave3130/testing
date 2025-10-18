# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll1l11_opy_ import bstack11ll1llll1l_opy_
from bstack_utils.constants import *
import json
class bstack1l11ll1111_opy_:
    def __init__(self, bstack11ll1111l1_opy_, bstack11ll1l11111_opy_):
        self.bstack11ll1111l1_opy_ = bstack11ll1111l1_opy_
        self.bstack11ll1l11111_opy_ = bstack11ll1l11111_opy_
        self.bstack11ll11llll1_opy_ = None
    def __call__(self):
        bstack11ll1l111l1_opy_ = {}
        while True:
            self.bstack11ll11llll1_opy_ = bstack11ll1l111l1_opy_.get(
                bstack1l1lll1_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧ᚜"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll1l1111l_opy_ = self.bstack11ll11llll1_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll1l1111l_opy_ > 0:
                sleep(bstack11ll1l1111l_opy_ / 1000)
            params = {
                bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᚝"): self.bstack11ll1111l1_opy_,
                bstack1l1lll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ᚞"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack1l1lll1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦ᚟") + bstack11ll11lllll_opy_ + bstack1l1lll1_opy_ (u"ࠥ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࠢᚠ")
            if self.bstack11ll1l11111_opy_.lower() == bstack1l1lll1_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࡷࠧᚡ"):
                bstack11ll1l111l1_opy_ = bstack11ll1llll1l_opy_.results(base_url, params)
            else:
                bstack11ll1l111l1_opy_ = bstack11ll1llll1l_opy_.bstack11ll11lll1l_opy_(base_url, params)
            if str(bstack11ll1l111l1_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᚢ"), bstack1l1lll1_opy_ (u"࠭࠲࠱࠲ࠪᚣ"))) != bstack1l1lll1_opy_ (u"ࠧ࠵࠲࠷ࠫᚤ"):
                break
        return bstack11ll1l111l1_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᚥ"), bstack11ll1l111l1_opy_)