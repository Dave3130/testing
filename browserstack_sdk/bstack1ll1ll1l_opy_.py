# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1llll1l1l_opy_, bstack1lll11ll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack1llll1l1l_opy_ = bstack1llll1l1l_opy_
        self.bstack1lll11ll1_opy_ = bstack1lll11ll1_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1ll1lll1_opy_(bstack111111111l_opy_):
        bstack1111111l11_opy_ = []
        if bstack111111111l_opy_:
            tokens = str(os.path.basename(bstack111111111l_opy_)).split(bstack11ll1l_opy_ (u"ࠦࡤࠨ჎"))
            camelcase_name = bstack11ll1l_opy_ (u"ࠧࠦࠢ჏").join(t.title() for t in tokens)
            suite_name, bstack11111111l1_opy_ = os.path.splitext(camelcase_name)
            bstack1111111l11_opy_.append(suite_name)
        return bstack1111111l11_opy_
    @staticmethod
    def bstack11111111ll_opy_(typename):
        if bstack11ll1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤა") in typename:
            return bstack11ll1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣბ")
        return bstack11ll1l_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤგ")