# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
from bstack_utils.constants import bstack11l11lll111_opy_
def bstack1l111l11l_opy_(bstack11ll11l1l11_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11l11ll11l_opy_
    host = bstack11l11ll11l_opy_(cli.config, [bstack1l1lll1_opy_ (u"ࠨࡡࡱ࡫ࡶࠦ≂"), bstack1l1lll1_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤ≃"), bstack1l1lll1_opy_ (u"ࠣࡣࡳ࡭ࠧ≄")], bstack11l11lll111_opy_)
    return bstack1l1lll1_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨ≅").format(host, bstack11ll11l1l11_opy_)