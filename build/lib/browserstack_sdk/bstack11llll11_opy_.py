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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1lll111l1_opy_, bstack1lll1l111_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll111l1_opy_ = bstack1lll111l1_opy_
        self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l11ll11_opy_(bstack1111111lll_opy_):
        bstack1111111l11_opy_ = []
        if bstack1111111lll_opy_:
            tokens = str(os.path.basename(bstack1111111lll_opy_)).split(bstack11ll_opy_ (u"ࠢࡠࠤჃ"))
            camelcase_name = bstack11ll_opy_ (u"ࠣࠢࠥჄ").join(t.title() for t in tokens)
            suite_name, bstack1111111l1l_opy_ = os.path.splitext(camelcase_name)
            bstack1111111l11_opy_.append(suite_name)
        return bstack1111111l11_opy_
    @staticmethod
    def bstack1111111ll1_opy_(typename):
        if bstack11ll_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧჅ") in typename:
            return bstack11ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ჆")
        return bstack11ll_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧჇ")