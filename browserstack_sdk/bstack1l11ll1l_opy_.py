# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack111l1l1l_opy_, bstack1111llll_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1l1l_opy_ = bstack111l1l1l_opy_
        self.bstack1111llll_opy_ = bstack1111llll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1lll1lll_opy_(bstack11111l1l11_opy_):
        bstack11111l11l1_opy_ = []
        if bstack11111l1l11_opy_:
            tokens = str(os.path.basename(bstack11111l1l11_opy_)).split(bstack1l_opy_ (u"ࠣࡡࠥႡ"))
            camelcase_name = bstack1l_opy_ (u"ࠤࠣࠦႢ").join(t.title() for t in tokens)
            suite_name, bstack11111l111l_opy_ = os.path.splitext(camelcase_name)
            bstack11111l11l1_opy_.append(suite_name)
        return bstack11111l11l1_opy_
    @staticmethod
    def bstack11111l11ll_opy_(typename):
        if bstack1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨႣ") in typename:
            return bstack1l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧႤ")
        return bstack1l_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨႥ")