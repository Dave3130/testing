# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1ll111l_opy_ import bstack11ll1l1l111_opy_
from bstack_utils.constants import *
import json
class bstack1l11l11lll_opy_:
    def __init__(self, bstack11lll1l1ll_opy_, bstack11ll11l1111_opy_):
        self.bstack11lll1l1ll_opy_ = bstack11lll1l1ll_opy_
        self.bstack11ll11l1111_opy_ = bstack11ll11l1111_opy_
        self.bstack11ll111llll_opy_ = None
    def __call__(self):
        bstack11ll11l111l_opy_ = {}
        while True:
            self.bstack11ll111llll_opy_ = bstack11ll11l111l_opy_.get(
                bstack11111_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛟ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll111ll1l_opy_ = self.bstack11ll111llll_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll111ll1l_opy_ > 0:
                sleep(bstack11ll111ll1l_opy_ / 1000)
            params = {
                bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᛠ"): self.bstack11lll1l1ll_opy_,
                bstack11111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᛡ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣᛢ") + bstack11ll111ll11_opy_ + bstack11111_opy_ (u"ࠢ࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࠦᛣ")
            if self.bstack11ll11l1111_opy_.lower() == bstack11111_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡴࠤᛤ"):
                bstack11ll11l111l_opy_ = bstack11ll1l1l111_opy_.results(base_url, params)
            else:
                bstack11ll11l111l_opy_ = bstack11ll1l1l111_opy_.bstack11ll111lll1_opy_(base_url, params)
            if str(bstack11ll11l111l_opy_.get(bstack11111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛥ"), bstack11111_opy_ (u"ࠪ࠶࠵࠶ࠧᛦ"))) != bstack11111_opy_ (u"ࠫ࠹࠶࠴ࠨᛧ"):
                break
        return bstack11ll11l111l_opy_.get(bstack11111_opy_ (u"ࠬࡪࡡࡵࡣࠪᛨ"), bstack11ll11l111l_opy_)