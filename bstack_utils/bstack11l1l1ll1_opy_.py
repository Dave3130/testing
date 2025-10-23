# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
from bstack_utils.constants import bstack11l11ll1ll1_opy_
def bstack1l11111l1_opy_(bstack11ll11l11l1_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack111ll111ll_opy_
    host = bstack111ll111ll_opy_(cli.config, [bstack11lll1_opy_ (u"ࠤࡤࡴ࡮ࡹࠢ≡"), bstack11lll1_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧ≢"), bstack11lll1_opy_ (u"ࠦࡦࡶࡩࠣ≣")], bstack11l11ll1ll1_opy_)
    return bstack11lll1_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫ≤").format(host, bstack11ll11l11l1_opy_)