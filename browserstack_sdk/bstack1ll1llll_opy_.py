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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1lll11l11_opy_, bstack1lll1l111_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll11l11_opy_ = bstack1lll11l11_opy_
        self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1lllll11_opy_(bstack1111111l11_opy_):
        bstack11111111l1_opy_ = []
        if bstack1111111l11_opy_:
            tokens = str(os.path.basename(bstack1111111l11_opy_)).split(bstack11111_opy_ (u"ࠣࡡࠥგ"))
            camelcase_name = bstack11111_opy_ (u"ࠤࠣࠦდ").join(t.title() for t in tokens)
            suite_name, bstack111111111l_opy_ = os.path.splitext(camelcase_name)
            bstack11111111l1_opy_.append(suite_name)
        return bstack11111111l1_opy_
    @staticmethod
    def bstack11111111ll_opy_(typename):
        if bstack11111_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨე") in typename:
            return bstack11111_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧვ")
        return bstack11111_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨზ")