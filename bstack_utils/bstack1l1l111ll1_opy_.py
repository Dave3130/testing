# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
from bstack_utils.constants import bstack11l1l1lll1l_opy_
def bstack111lll1ll_opy_(bstack11ll11lll11_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11l11111l_opy_
    host = bstack11l11111l_opy_(cli.config, [bstack1ll11_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ≄"), bstack1ll11_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ≅"), bstack1ll11_opy_ (u"ࠥࡥࡵ࡯ࠢ≆")], bstack11l1l1lll1l_opy_)
    return bstack1ll11_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ≇").format(host, bstack11ll11lll11_opy_)