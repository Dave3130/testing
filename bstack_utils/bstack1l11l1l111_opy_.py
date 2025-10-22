# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
from bstack_utils.constants import bstack11l1l11ll1l_opy_
def bstack1l111ll1l1_opy_(bstack11ll11l1111_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11l111l1ll_opy_
    host = bstack11l111l1ll_opy_(cli.config, [bstack1lllll1l_opy_ (u"ࠨࡡࡱ࡫ࡶࠦ≥"), bstack1lllll1l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤ≦"), bstack1lllll1l_opy_ (u"ࠣࡣࡳ࡭ࠧ≧")], bstack11l1l11ll1l_opy_)
    return bstack1lllll1l_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨ≨").format(host, bstack11ll11l1111_opy_)