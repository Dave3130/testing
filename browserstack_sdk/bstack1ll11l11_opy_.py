# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1111l1ll_opy_, bstack111l11ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l1ll_opy_ = bstack1111l1ll_opy_
        self.bstack111l11ll_opy_ = bstack111l11ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1llll111_opy_(bstack11111l111l_opy_):
        bstack11111l11ll_opy_ = []
        if bstack11111l111l_opy_:
            tokens = str(os.path.basename(bstack11111l111l_opy_)).split(bstack1ll1ll1_opy_ (u"ࠢࡠࠤႠ"))
            camelcase_name = bstack1ll1ll1_opy_ (u"ࠣࠢࠥႡ").join(t.title() for t in tokens)
            suite_name, bstack11111l1l11_opy_ = os.path.splitext(camelcase_name)
            bstack11111l11ll_opy_.append(suite_name)
        return bstack11111l11ll_opy_
    @staticmethod
    def bstack11111l11l1_opy_(typename):
        if bstack1ll1ll1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧႢ") in typename:
            return bstack1ll1ll1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦႣ")
        return bstack1ll1ll1_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧႤ")