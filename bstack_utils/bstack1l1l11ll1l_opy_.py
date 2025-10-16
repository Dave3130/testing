# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
from bstack_utils.constants import bstack11l1l1lllll_opy_
def bstack111l11l111_opy_(bstack11ll11ll11l_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11l1l1l11_opy_
    host = bstack11l1l1l11_opy_(cli.config, [bstack1ll1ll1_opy_ (u"ࠦࡦࡶࡩࡴࠤ≇"), bstack1ll1ll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ≈"), bstack1ll1ll1_opy_ (u"ࠨࡡࡱ࡫ࠥ≉")], bstack11l1l1lllll_opy_)
    return bstack1ll1ll1_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭≊").format(host, bstack11ll11ll11l_opy_)