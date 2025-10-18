# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1llll1l1l_opy_, bstack1lll1llll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1llll1l1l_opy_ = bstack1llll1l1l_opy_
        self.bstack1lll1llll_opy_ = bstack1lll1llll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1l1l11_opy_(bstack1111111ll1_opy_):
        bstack1111111l1l_opy_ = []
        if bstack1111111ll1_opy_:
            tokens = str(os.path.basename(bstack1111111ll1_opy_)).split(bstack11l111_opy_ (u"ࠧࡥࠢჁ"))
            camelcase_name = bstack11l111_opy_ (u"ࠨࠠࠣჂ").join(t.title() for t in tokens)
            suite_name, bstack111111l111_opy_ = os.path.splitext(camelcase_name)
            bstack1111111l1l_opy_.append(suite_name)
        return bstack1111111l1l_opy_
    @staticmethod
    def bstack1111111lll_opy_(typename):
        if bstack11l111_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥჃ") in typename:
            return bstack11l111_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤჄ")
        return bstack11l111_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥჅ")