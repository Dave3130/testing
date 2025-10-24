# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
from bstack_utils.constants import bstack11l11lll11l_opy_
def bstack1l111111l1_opy_(bstack11ll11l1l11_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11l1lll1l_opy_
    host = bstack11l1lll1l_opy_(cli.config, [bstack11l11l1_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ≛"), bstack11l11l1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ≜"), bstack11l11l1_opy_ (u"ࠧࡧࡰࡪࠤ≝")], bstack11l11lll11l_opy_)
    return bstack11l11l1_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ≞").format(host, bstack11ll11l1l11_opy_)