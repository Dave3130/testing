# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1lll1l1_opy_ import bstack11ll1ll1l11_opy_
from bstack_utils.constants import *
import json
class bstack1111ll1l1l_opy_:
    def __init__(self, bstack1l1ll11l1l_opy_, bstack11ll11l11ll_opy_):
        self.bstack1l1ll11l1l_opy_ = bstack1l1ll11l1l_opy_
        self.bstack11ll11l11ll_opy_ = bstack11ll11l11ll_opy_
        self.bstack11ll11l111l_opy_ = None
    def __call__(self):
        bstack11ll11l1ll1_opy_ = {}
        while True:
            self.bstack11ll11l111l_opy_ = bstack11ll11l1ll1_opy_.get(
                bstack11l11ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛐ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11l1l11_opy_ = self.bstack11ll11l111l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11l1l11_opy_ > 0:
                sleep(bstack11ll11l1l11_opy_ / 1000)
            params = {
                bstack11l11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᛑ"): self.bstack1l1ll11l1l_opy_,
                bstack11l11ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᛒ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11l11ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᛓ") + bstack11ll11l1l1l_opy_ + bstack11l11ll_opy_ (u"ࠨ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࠥᛔ")
            if self.bstack11ll11l11ll_opy_.lower() == bstack11l11ll_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡳࠣᛕ"):
                bstack11ll11l1ll1_opy_ = bstack11ll1ll1l11_opy_.results(base_url, params)
            else:
                bstack11ll11l1ll1_opy_ = bstack11ll1ll1l11_opy_.bstack11ll11l11l1_opy_(base_url, params)
            if str(bstack11ll11l1ll1_opy_.get(bstack11l11ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᛖ"), bstack11l11ll_opy_ (u"ࠩ࠵࠴࠵࠭ᛗ"))) != bstack11l11ll_opy_ (u"ࠪ࠸࠵࠺ࠧᛘ"):
                break
        return bstack11ll11l1ll1_opy_.get(bstack11l11ll_opy_ (u"ࠫࡩࡧࡴࡢࠩᛙ"), bstack11ll11l1ll1_opy_)