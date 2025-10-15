# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack111l1111_opy_, bstack111ll1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1111_opy_ = bstack111l1111_opy_
        self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l111lll_opy_(bstack11111l1111_opy_):
        bstack11111l111l_opy_ = []
        if bstack11111l1111_opy_:
            tokens = str(os.path.basename(bstack11111l1111_opy_)).split(bstack1ll1l_opy_ (u"ࠢࡠࠤ႙"))
            camelcase_name = bstack1ll1l_opy_ (u"ࠣࠢࠥႚ").join(t.title() for t in tokens)
            suite_name, bstack111111llll_opy_ = os.path.splitext(camelcase_name)
            bstack11111l111l_opy_.append(suite_name)
        return bstack11111l111l_opy_
    @staticmethod
    def bstack11111l11l1_opy_(typename):
        if bstack1ll1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧႛ") in typename:
            return bstack1ll1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦႜ")
        return bstack1ll1l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧႝ")