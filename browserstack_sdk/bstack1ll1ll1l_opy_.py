# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1lllll11l_opy_, bstack111ll1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
        self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1ll1l111_opy_(bstack11111l1111_opy_):
        bstack11111l111l_opy_ = []
        if bstack11111l1111_opy_:
            tokens = str(os.path.basename(bstack11111l1111_opy_)).split(bstack11111_opy_ (u"ࠥࡣࠧႎ"))
            camelcase_name = bstack11111_opy_ (u"ࠦࠥࠨႏ").join(t.title() for t in tokens)
            suite_name, bstack111111llll_opy_ = os.path.splitext(camelcase_name)
            bstack11111l111l_opy_.append(suite_name)
        return bstack11111l111l_opy_
    @staticmethod
    def bstack111111lll1_opy_(typename):
        if bstack11111_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣ႐") in typename:
            return bstack11111_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢ႑")
        return bstack11111_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣ႒")