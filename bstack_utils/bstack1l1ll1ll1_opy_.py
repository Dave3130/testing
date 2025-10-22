# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
from bstack_utils.constants import bstack11l1l111lll_opy_
def bstack11llllll11_opy_(bstack11ll111ll11_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1l11ll1111_opy_
    host = bstack1l11ll1111_opy_(cli.config, [bstack1l111ll_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ≢"), bstack1l111ll_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ≣"), bstack1l111ll_opy_ (u"ࠧࡧࡰࡪࠤ≤")], bstack11l1l111lll_opy_)
    return bstack1l111ll_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ≥").format(host, bstack11ll111ll11_opy_)