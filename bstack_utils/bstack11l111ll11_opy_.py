# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll11ll_opy_ import bstack11ll1l111l1_opy_
from bstack_utils.constants import *
import json
class bstack1ll11l111l_opy_:
    def __init__(self, bstack111lll111_opy_, bstack11ll111lll1_opy_):
        self.bstack111lll111_opy_ = bstack111lll111_opy_
        self.bstack11ll111lll1_opy_ = bstack11ll111lll1_opy_
        self.bstack11ll11l1111_opy_ = None
    def __call__(self):
        bstack11ll111ll11_opy_ = {}
        while True:
            self.bstack11ll11l1111_opy_ = bstack11ll111ll11_opy_.get(
                bstack11ll1ll_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛠ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll111ll1l_opy_ = self.bstack11ll11l1111_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll111ll1l_opy_ > 0:
                sleep(bstack11ll111ll1l_opy_ / 1000)
            params = {
                bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᛡ"): self.bstack111lll111_opy_,
                bstack11ll1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᛢ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11ll1ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤᛣ") + bstack11ll11l111l_opy_ + bstack11ll1ll_opy_ (u"ࠣ࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࠧᛤ")
            if self.bstack11ll111lll1_opy_.lower() == bstack11ll1ll_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡵࠥᛥ"):
                bstack11ll111ll11_opy_ = bstack11ll1l111l1_opy_.results(base_url, params)
            else:
                bstack11ll111ll11_opy_ = bstack11ll1l111l1_opy_.bstack11ll111llll_opy_(base_url, params)
            if str(bstack11ll111ll11_opy_.get(bstack11ll1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛦ"), bstack11ll1ll_opy_ (u"ࠫ࠷࠶࠰ࠨᛧ"))) != bstack11ll1ll_opy_ (u"ࠬ࠺࠰࠵ࠩᛨ"):
                break
        return bstack11ll111ll11_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡤࡢࡶࡤࠫᛩ"), bstack11ll111ll11_opy_)