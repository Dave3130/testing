# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1lll1lll1_opy_, bstack1lllll11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll1lll1_opy_ = bstack1lll1lll1_opy_
        self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1ll11l_opy_(bstack11111l111l_opy_):
        bstack111111llll_opy_ = []
        if bstack11111l111l_opy_:
            tokens = str(os.path.basename(bstack11111l111l_opy_)).split(bstack1l1lll1_opy_ (u"ࠣࡡࠥႚ"))
            camelcase_name = bstack1l1lll1_opy_ (u"ࠤࠣࠦႛ").join(t.title() for t in tokens)
            suite_name, bstack111111lll1_opy_ = os.path.splitext(camelcase_name)
            bstack111111llll_opy_.append(suite_name)
        return bstack111111llll_opy_
    @staticmethod
    def bstack11111l1111_opy_(typename):
        if bstack1l1lll1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨႜ") in typename:
            return bstack1l1lll1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧႝ")
        return bstack1l1lll1_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨ႞")