# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from bstack_utils.constants import bstack11l1l111l1l_opy_
def bstack1ll1ll11ll_opy_(bstack11ll11l1lll_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1ll11l1l1_opy_
    host = bstack1ll11l1l1_opy_(cli.config, [bstack1ll1l_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ∿"), bstack1ll1l_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ≀"), bstack1ll1l_opy_ (u"ࠧࡧࡰࡪࠤ≁")], bstack11l1l111l1l_opy_)
    return bstack1ll1l_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ≂").format(host, bstack11ll11l1lll_opy_)