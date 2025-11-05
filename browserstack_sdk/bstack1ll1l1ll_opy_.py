# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1lll11l1l_opy_, bstack1lll1l1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll11l1l_opy_ = bstack1lll11l1l_opy_
        self.bstack1lll1l1ll_opy_ = bstack1lll1l1ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1lll1lll_opy_(bstack1111111l1l_opy_):
        bstack111111l111_opy_ = []
        if bstack1111111l1l_opy_:
            tokens = str(os.path.basename(bstack1111111l1l_opy_)).split(bstack1lll11l_opy_ (u"ࠥࡣࠧႸ"))
            camelcase_name = bstack1lll11l_opy_ (u"ࠦࠥࠨႹ").join(t.title() for t in tokens)
            suite_name, bstack1111111ll1_opy_ = os.path.splitext(camelcase_name)
            bstack111111l111_opy_.append(suite_name)
        return bstack111111l111_opy_
    @staticmethod
    def bstack1111111lll_opy_(typename):
        if bstack1lll11l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣႺ") in typename:
            return bstack1lll11l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢႻ")
        return bstack1lll11l_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣႼ")