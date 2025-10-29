# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
from bstack_utils.constants import bstack11l11l1llll_opy_
def bstack1l1lll1l11_opy_(bstack11ll111l11l_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1lll1l11l1_opy_
    host = bstack1lll1l11l1_opy_(cli.config, [bstack11ll1l_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ⊃"), bstack11ll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ⊄"), bstack11ll1l_opy_ (u"ࠥࡥࡵ࡯ࠢ⊅")], bstack11l11l1llll_opy_)
    return bstack11ll1l_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ⊆").format(host, bstack11ll111l11l_opy_)