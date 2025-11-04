# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
from bstack_utils.constants import bstack11l11ll111l_opy_
def bstack1llll11l11_opy_(bstack11ll111l111_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11llll111_opy_
    host = bstack11llll111_opy_(cli.config, [bstack11l1111_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ⊗"), bstack11l1111_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ⊘"), bstack11l1111_opy_ (u"ࠤࡤࡴ࡮ࠨ⊙")], bstack11l11ll111l_opy_)
    return bstack11l1111_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩ⊚").format(host, bstack11ll111l111_opy_)