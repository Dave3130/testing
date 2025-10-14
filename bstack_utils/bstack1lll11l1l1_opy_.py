# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
from bstack_utils.constants import bstack11l11ll1ll1_opy_
def bstack1l11l1l1ll_opy_(bstack11ll11l1ll1_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack111ll1l1ll_opy_
    host = bstack111ll1l1ll_opy_(cli.config, [bstack11l1l11_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ∽"), bstack11l1l11_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ∾"), bstack11l1l11_opy_ (u"ࠥࡥࡵ࡯ࠢ∿")], bstack11l11ll1ll1_opy_)
    return bstack11l1l11_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ≀").format(host, bstack11ll11l1ll1_opy_)