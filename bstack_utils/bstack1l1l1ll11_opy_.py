# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
from bstack_utils.constants import bstack11l11ll11ll_opy_
def bstack1ll11llll_opy_(bstack11ll111l11l_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack11ll11l111_opy_
    host = bstack11ll11l111_opy_(cli.config, [bstack11111_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ⊘"), bstack11111_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ⊙"), bstack11111_opy_ (u"ࠥࡥࡵ࡯ࠢ⊚")], bstack11l11ll11ll_opy_)
    return bstack11111_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ⊛").format(host, bstack11ll111l11l_opy_)