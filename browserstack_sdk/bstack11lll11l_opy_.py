# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11111l11_opy_, bstack1lll111ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack11111l11_opy_ = bstack11111l11_opy_
        self.bstack1lll111ll_opy_ = bstack1lll111ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l11l11l_opy_(bstack1111111l11_opy_):
        bstack1111111lll_opy_ = []
        if bstack1111111l11_opy_:
            tokens = str(os.path.basename(bstack1111111l11_opy_)).split(bstack111l1l_opy_ (u"ࠢࡠࠤႼ"))
            camelcase_name = bstack111l1l_opy_ (u"ࠣࠢࠥႽ").join(t.title() for t in tokens)
            suite_name, bstack1111111ll1_opy_ = os.path.splitext(camelcase_name)
            bstack1111111lll_opy_.append(suite_name)
        return bstack1111111lll_opy_
    @staticmethod
    def bstack1111111l1l_opy_(typename):
        if bstack111l1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧႾ") in typename:
            return bstack111l1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦႿ")
        return bstack111l1l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧჀ")