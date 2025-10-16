# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11lll111l1l_opy_ import bstack11ll1lll111_opy_
from bstack_utils.constants import *
import json
class bstack1l1ll1ll1l_opy_:
    def __init__(self, bstack11l1l1l11_opy_, bstack11ll1l11l1l_opy_):
        self.bstack11l1l1l11_opy_ = bstack11l1l1l11_opy_
        self.bstack11ll1l11l1l_opy_ = bstack11ll1l11l1l_opy_
        self.bstack11ll1l11l11_opy_ = None
    def __call__(self):
        bstack11ll1l1111l_opy_ = {}
        while True:
            self.bstack11ll1l11l11_opy_ = bstack11ll1l1111l_opy_.get(
                bstack1l_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᚣ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll1l111l1_opy_ = self.bstack11ll1l11l11_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll1l111l1_opy_ > 0:
                sleep(bstack11ll1l111l1_opy_ / 1000)
            params = {
                bstack1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᚤ"): self.bstack11l1l1l11_opy_,
                bstack1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᚥ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᚦ") + bstack11ll1l11111_opy_ + bstack1l_opy_ (u"ࠥ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࠢᚧ")
            if self.bstack11ll1l11l1l_opy_.lower() == bstack1l_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࡷࠧᚨ"):
                bstack11ll1l1111l_opy_ = bstack11ll1lll111_opy_.results(base_url, params)
            else:
                bstack11ll1l1111l_opy_ = bstack11ll1lll111_opy_.bstack11ll1l111ll_opy_(base_url, params)
            if str(bstack11ll1l1111l_opy_.get(bstack1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᚩ"), bstack1l_opy_ (u"࠭࠲࠱࠲ࠪᚪ"))) != bstack1l_opy_ (u"ࠧ࠵࠲࠷ࠫᚫ"):
                break
        return bstack11ll1l1111l_opy_.get(bstack1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᚬ"), bstack11ll1l1111l_opy_)