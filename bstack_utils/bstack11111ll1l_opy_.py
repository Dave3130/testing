# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from bstack_utils.constants import bstack11l1l111ll1_opy_
def bstack1lll1ll11l_opy_(bstack11ll11l1ll1_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1l111ll111_opy_
    host = bstack1l111ll111_opy_(cli.config, [bstack1lllll1_opy_ (u"ࠤࡤࡴ࡮ࡹࠢ≅"), bstack1lllll1_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧ≆"), bstack1lllll1_opy_ (u"ࠦࡦࡶࡩࠣ≇")], bstack11l1l111ll1_opy_)
    return bstack1lllll1_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫ≈").format(host, bstack11ll11l1ll1_opy_)