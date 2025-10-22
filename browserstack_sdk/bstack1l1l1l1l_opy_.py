# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1lll111l1_opy_, bstack111lll11_opy_):
        self.args = args
        self.logger = logger
        self.bstack1lll111l1_opy_ = bstack1lll111l1_opy_
        self.bstack111lll11_opy_ = bstack111lll11_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1ll11111_opy_(bstack1111111l1l_opy_):
        bstack1111111ll1_opy_ = []
        if bstack1111111l1l_opy_:
            tokens = str(os.path.basename(bstack1111111l1l_opy_)).split(bstack1lllll1l_opy_ (u"ࠥࡣࠧႿ"))
            camelcase_name = bstack1lllll1l_opy_ (u"ࠦࠥࠨჀ").join(t.title() for t in tokens)
            suite_name, bstack1111111lll_opy_ = os.path.splitext(camelcase_name)
            bstack1111111ll1_opy_.append(suite_name)
        return bstack1111111ll1_opy_
    @staticmethod
    def bstack111111l111_opy_(typename):
        if bstack1lllll1l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣჁ") in typename:
            return bstack1lllll1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢჂ")
        return bstack1lllll1l_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣჃ")