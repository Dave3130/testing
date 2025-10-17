# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
from bstack_utils.constants import bstack11l1l1l1ll1_opy_
def bstack11ll1l1l1_opy_(bstack11ll11ll111_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack111l11l1l_opy_
    host = bstack111l11l1l_opy_(cli.config, [bstack11l111_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ∵"), bstack11l111_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ∶"), bstack11l111_opy_ (u"ࠤࡤࡴ࡮ࠨ∷")], bstack11l1l1l1ll1_opy_)
    return bstack11l111_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩ∸").format(host, bstack11ll11ll111_opy_)