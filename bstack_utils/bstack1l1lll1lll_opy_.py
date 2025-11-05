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
from bstack_utils.constants import bstack11l11llll11_opy_
def bstack11l1l1l1l1_opy_(bstack11ll11111ll_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack111l111l11_opy_
    host = bstack111l111l11_opy_(cli.config, [bstack11ll1ll_opy_ (u"ࠤࡤࡴ࡮ࡹࠢ⊙"), bstack11ll1ll_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧ⊚"), bstack11ll1ll_opy_ (u"ࠦࡦࡶࡩࠣ⊛")], bstack11l11llll11_opy_)
    return bstack11ll1ll_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫ⊜").format(host, bstack11ll11111ll_opy_)