# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
from time import sleep
from datetime import datetime
from urllib.parse import urlencode
from bstack_utils.bstack11ll1l11l1l_opy_ import bstack11ll1l1l1l1_opy_
from bstack_utils.constants import *
import json
class bstack1ll1111ll_opy_:
    def __init__(self, bstack1l11l1l111_opy_, bstack11ll111ll11_opy_):
        self.bstack1l11l1l111_opy_ = bstack1l11l1l111_opy_
        self.bstack11ll111ll11_opy_ = bstack11ll111ll11_opy_
        self.bstack11ll11l111l_opy_ = None
    def __call__(self):
        bstack11ll111llll_opy_ = {}
        while True:
            self.bstack11ll11l111l_opy_ = bstack11ll111llll_opy_.get(
                bstack11l1111_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛟ"),
                int(datetime.now().timestamp() * 1000)
            )
            bstack11ll11l1111_opy_ = self.bstack11ll11l111l_opy_ - int(datetime.now().timestamp() * 1000)
            if bstack11ll11l1111_opy_ > 0:
                sleep(bstack11ll11l1111_opy_ / 1000)
            params = {
                bstack11l1111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᛠ"): self.bstack1l11l1l111_opy_,
                bstack11l1111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᛡ"): int(datetime.now().timestamp() * 1000)
            }
            base_url = bstack11l1111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣᛢ") + bstack11ll111ll1l_opy_ + bstack11l1111_opy_ (u"ࠢ࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࠦᛣ")
            if self.bstack11ll111ll11_opy_.lower() == bstack11l1111_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡴࠤᛤ"):
                bstack11ll111llll_opy_ = bstack11ll1l1l1l1_opy_.results(base_url, params)
            else:
                bstack11ll111llll_opy_ = bstack11ll1l1l1l1_opy_.bstack11ll111lll1_opy_(base_url, params)
            if str(bstack11ll111llll_opy_.get(bstack11l1111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛥ"), bstack11l1111_opy_ (u"ࠪ࠶࠵࠶ࠧᛦ"))) != bstack11l1111_opy_ (u"ࠫ࠹࠶࠴ࠨᛧ"):
                break
        return bstack11ll111llll_opy_.get(bstack11l1111_opy_ (u"ࠬࡪࡡࡵࡣࠪᛨ"), bstack11ll111llll_opy_)