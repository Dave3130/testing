# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1llllllll_opy_, bstack1llll1111_opy_):
        self.args = args
        self.logger = logger
        self.bstack1llllllll_opy_ = bstack1llllllll_opy_
        self.bstack1llll1111_opy_ = bstack1llll1111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l111l1l_opy_(bstack11111111l1_opy_):
        bstack1111111l11_opy_ = []
        if bstack11111111l1_opy_:
            tokens = str(os.path.basename(bstack11111111l1_opy_)).split(bstack11l11ll_opy_ (u"ࠦࡤࠨ჎"))
            camelcase_name = bstack11l11ll_opy_ (u"ࠧࠦࠢ჏").join(t.title() for t in tokens)
            suite_name, bstack111111111l_opy_ = os.path.splitext(camelcase_name)
            bstack1111111l11_opy_.append(suite_name)
        return bstack1111111l11_opy_
    @staticmethod
    def bstack11111111ll_opy_(typename):
        if bstack11l11ll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤა") in typename:
            return bstack11l11ll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣბ")
        return bstack11l11ll_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤგ")