# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1l1lll1_opy_ import bstack11ll1l1ll11_opy_
from bstack_utils.constants import *
import json
class bstack1lllll1l11_opy_:
    def __init__(self, bstack1l11111ll_opy_, bstack11ll11l111l_opy_):
        self.bstack1l11111ll_opy_ = bstack1l11111ll_opy_
        self.bstack11ll11l111l_opy_ = bstack11ll11l111l_opy_
        self.bstack11ll11l1l1l_opy_ = None
    def __call__(self):
        bstack11ll11l1l11_opy_ = {}
        while True:
            self.bstack11ll11l1l1l_opy_ = bstack11ll11l1l11_opy_.get(
                bstack11ll1l_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛐ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11l1ll1_opy_ = self.bstack11ll11l1l1l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11l1ll1_opy_ > 0:
                sleep(bstack11ll11l1ll1_opy_ / 1000)
            params = {
                bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᛑ"): self.bstack1l11111ll_opy_,
                bstack11ll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᛒ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᛓ") + bstack11ll11l11ll_opy_ + bstack11ll1l_opy_ (u"ࠨ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࠥᛔ")
            if self.bstack11ll11l111l_opy_.lower() == bstack11ll1l_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡳࠣᛕ"):
                bstack11ll11l1l11_opy_ = bstack11ll1l1ll11_opy_.results(base_url, params)
            else:
                bstack11ll11l1l11_opy_ = bstack11ll1l1ll11_opy_.bstack11ll11l11l1_opy_(base_url, params)
            if str(bstack11ll11l1l11_opy_.get(bstack11ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᛖ"), bstack11ll1l_opy_ (u"ࠩ࠵࠴࠵࠭ᛗ"))) != bstack11ll1l_opy_ (u"ࠪ࠸࠵࠺ࠧᛘ"):
                break
        return bstack11ll11l1l11_opy_.get(bstack11ll1l_opy_ (u"ࠫࡩࡧࡴࡢࠩᛙ"), bstack11ll11l1l11_opy_)