# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
from bstack_utils.constants import bstack11l1l1l11l1_opy_
def bstack1l11l1111_opy_(bstack11ll111l11l_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1lllllll11_opy_
    host = bstack1lllllll11_opy_(cli.config, [bstack11l1l11_opy_ (u"ࠤࡤࡴ࡮ࡹࠢ≡"), bstack11l1l11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧ≢"), bstack11l1l11_opy_ (u"ࠦࡦࡶࡩࠣ≣")], bstack11l1l1l11l1_opy_)
    return bstack11l1l11_opy_ (u"ࠬࢁࡽ࠰ࡽࢀࠫ≤").format(host, bstack11ll111l11l_opy_)