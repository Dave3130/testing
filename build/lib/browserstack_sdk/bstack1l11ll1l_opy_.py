# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack111l1lll_opy_, bstack1lll1ll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l1lll_opy_ = bstack111l1lll_opy_
        self.bstack1lll1ll1l_opy_ = bstack1lll1ll1l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1ll11l_opy_(bstack1111111ll1_opy_):
        bstack1111111lll_opy_ = []
        if bstack1111111ll1_opy_:
            tokens = str(os.path.basename(bstack1111111ll1_opy_)).split(bstack11lll1_opy_ (u"ࠨ࡟ࠣႻ"))
            camelcase_name = bstack11lll1_opy_ (u"ࠢࠡࠤႼ").join(t.title() for t in tokens)
            suite_name, bstack111111l111_opy_ = os.path.splitext(camelcase_name)
            bstack1111111lll_opy_.append(suite_name)
        return bstack1111111lll_opy_
    @staticmethod
    def bstack1111111l1l_opy_(typename):
        if bstack11lll1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦႽ") in typename:
            return bstack11lll1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥႾ")
        return bstack11lll1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦႿ")