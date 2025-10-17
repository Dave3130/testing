# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1lllll11l_opy_, bstack11l1l11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
        self.bstack11l1l11l_opy_ = bstack11l1l11l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1lllll11_opy_(bstack111111ll1l_opy_):
        bstack111111llll_opy_ = []
        if bstack111111ll1l_opy_:
            tokens = str(os.path.basename(bstack111111ll1l_opy_)).split(bstack11l111_opy_ (u"ࠥࡣࠧႎ"))
            camelcase_name = bstack11l111_opy_ (u"ࠦࠥࠨႏ").join(t.title() for t in tokens)
            suite_name, bstack111111lll1_opy_ = os.path.splitext(camelcase_name)
            bstack111111llll_opy_.append(suite_name)
        return bstack111111llll_opy_
    @staticmethod
    def bstack11111l1111_opy_(typename):
        if bstack11l111_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣ႐") in typename:
            return bstack11l111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢ႑")
        return bstack11l111_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣ႒")