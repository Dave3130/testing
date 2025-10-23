# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
from bstack_utils.constants import bstack11l1l1ll111_opy_
def bstack11ll11l11_opy_(bstack11ll11ll111_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1lll1111l_opy_
    host = bstack1lll1111l_opy_(cli.config, [bstack111111l_opy_ (u"ࠧࡧࡰࡪࡵࠥ∺"), bstack111111l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣ∻"), bstack111111l_opy_ (u"ࠢࡢࡲ࡬ࠦ∼")], bstack11l1l1ll111_opy_)
    return bstack111111l_opy_ (u"ࠨࡽࢀ࠳ࢀࢃࠧ∽").format(host, bstack11ll11ll111_opy_)