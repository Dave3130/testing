# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
from bstack_utils.constants import bstack11l11llllll_opy_
def bstack1ll1l1l11_opy_(bstack11ll11ll111_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11lllll1ll_opy_
    host = bstack11lllll1ll_opy_(cli.config, [bstack11111_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ∵"), bstack11111_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ∶"), bstack11111_opy_ (u"ࠤࡤࡴ࡮ࠨ∷")], bstack11l11llllll_opy_)
    return bstack11111_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩ∸").format(host, bstack11ll11ll111_opy_)