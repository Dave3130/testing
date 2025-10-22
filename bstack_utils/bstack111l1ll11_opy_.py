# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
from bstack_utils.constants import bstack11l1l111ll1_opy_
def bstack1l1lll1ll_opy_(bstack11ll111l1ll_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1l1ll1ll1l_opy_
    host = bstack1l1ll1ll1l_opy_(cli.config, [bstack111l1l_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ≢"), bstack111l1l_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ≣"), bstack111l1l_opy_ (u"ࠧࡧࡰࡪࠤ≤")], bstack11l1l111ll1_opy_)
    return bstack111l1l_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ≥").format(host, bstack11ll111l1ll_opy_)