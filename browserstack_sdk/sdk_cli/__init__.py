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