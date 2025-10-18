# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
from bstack_utils.constants import bstack11l1l1l1111_opy_
def bstack1lll11l111_opy_(bstack11ll111l11l_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack111ll111l1_opy_
    host = bstack111ll111l1_opy_(cli.config, [bstack11ll_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ≩"), bstack11ll_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ≪"), bstack11ll_opy_ (u"ࠧࡧࡰࡪࠤ≫")], bstack11l1l1l1111_opy_)
    return bstack11ll_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ≬").format(host, bstack11ll111l11l_opy_)