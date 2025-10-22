# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1lll1l111_opy_, bstack1lll11l11_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
        self.bstack1lll11l11_opy_ = bstack1lll11l11_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l11l11l_opy_(bstack1111111ll1_opy_):
        bstack1111111l11_opy_ = []
        if bstack1111111ll1_opy_:
            tokens = str(os.path.basename(bstack1111111ll1_opy_)).split(bstack1l111ll_opy_ (u"ࠢࡠࠤႼ"))
            camelcase_name = bstack1l111ll_opy_ (u"ࠣࠢࠥႽ").join(t.title() for t in tokens)
            suite_name, bstack1111111lll_opy_ = os.path.splitext(camelcase_name)
            bstack1111111l11_opy_.append(suite_name)
        return bstack1111111l11_opy_
    @staticmethod
    def bstack1111111l1l_opy_(typename):
        if bstack1l111ll_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧႾ") in typename:
            return bstack1l111ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦႿ")
        return bstack1l111ll_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧჀ")