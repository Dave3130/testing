# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
from bstack_utils.constants import bstack11l1l1l1l11_opy_
def bstack11l1l11l1_opy_(bstack11ll111ll11_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack111111ll11_opy_
    host = bstack111111ll11_opy_(cli.config, [bstack11l111_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ≧"), bstack11l111_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ≨"), bstack11l111_opy_ (u"ࠥࡥࡵ࡯ࠢ≩")], bstack11l1l1l1l11_opy_)
    return bstack11l111_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ≪").format(host, bstack11ll111ll11_opy_)