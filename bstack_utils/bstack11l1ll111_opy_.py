# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
from bstack_utils.constants import bstack11l11ll1l11_opy_
def bstack1l11lll1l1_opy_(bstack11ll111llll_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11111l111l_opy_
    host = bstack11111l111l_opy_(cli.config, [bstack11l11ll_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ⊂"), bstack11l11ll_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ⊃"), bstack11l11ll_opy_ (u"ࠤࡤࡴ࡮ࠨ⊄")], bstack11l11ll1l11_opy_)
    return bstack11l11ll_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩ⊅").format(host, bstack11ll111llll_opy_)