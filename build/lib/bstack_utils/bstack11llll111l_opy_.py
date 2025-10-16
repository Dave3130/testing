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
from bstack_utils.constants import bstack11l11lll1l1_opy_
def bstack11lllll11_opy_(bstack11ll11ll111_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1l111ll1ll_opy_
    host = bstack1l111ll1ll_opy_(cli.config, [bstack1l_opy_ (u"ࠦࡦࡶࡩࡴࠤ≇"), bstack1l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ≈"), bstack1l_opy_ (u"ࠨࡡࡱ࡫ࠥ≉")], bstack11l11lll1l1_opy_)
    return bstack1l_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭≊").format(host, bstack11ll11ll111_opy_)