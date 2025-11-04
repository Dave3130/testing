# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack111ll11l_opy_, bstack1lll1l1l1_opy_):
        self.args = args
        self.logger = logger
        self.bstack111ll11l_opy_ = bstack111ll11l_opy_
        self.bstack1lll1l1l1_opy_ = bstack1lll1l1l1_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1lll1ll1_opy_(bstack111111111l_opy_):
        bstack1111111l11_opy_ = []
        if bstack111111111l_opy_:
            tokens = str(os.path.basename(bstack111111111l_opy_)).split(bstack11l1111_opy_ (u"ࠣࡡࠥგ"))
            camelcase_name = bstack11l1111_opy_ (u"ࠤࠣࠦდ").join(t.title() for t in tokens)
            suite_name, bstack11111111l1_opy_ = os.path.splitext(camelcase_name)
            bstack1111111l11_opy_.append(suite_name)
        return bstack1111111l11_opy_
    @staticmethod
    def bstack11111111ll_opy_(typename):
        if bstack11l1111_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨე") in typename:
            return bstack11l1111_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧვ")
        return bstack11l1111_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨზ")