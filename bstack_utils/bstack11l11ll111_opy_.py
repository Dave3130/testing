# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
from bstack_utils.constants import bstack11l1l111111_opy_
def bstack11111lll11_opy_(bstack11ll111l1ll_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11llll111_opy_
    host = bstack11llll111_opy_(cli.config, [bstack1lll11l_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ≾"), bstack1lll11l_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ≿"), bstack1lll11l_opy_ (u"ࠧࡧࡰࡪࠤ⊀")], bstack11l1l111111_opy_)
    return bstack1lll11l_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ⊁").format(host, bstack11ll111l1ll_opy_)