# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1111l111_opy_, bstack111l1lll_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l111_opy_ = bstack1111l111_opy_
        self.bstack111l1lll_opy_ = bstack111l1lll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1lll1l_opy_(bstack111111l111_opy_):
        bstack111111l1l1_opy_ = []
        if bstack111111l111_opy_:
            tokens = str(os.path.basename(bstack111111l111_opy_)).split(bstack11l11l1_opy_ (u"ࠨ࡟ࠣႴ"))
            camelcase_name = bstack11l11l1_opy_ (u"ࠢࠡࠤႵ").join(t.title() for t in tokens)
            suite_name, bstack111111l11l_opy_ = os.path.splitext(camelcase_name)
            bstack111111l1l1_opy_.append(suite_name)
        return bstack111111l1l1_opy_
    @staticmethod
    def bstack111111l1ll_opy_(typename):
        if bstack11l11l1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦႶ") in typename:
            return bstack11l11l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥႷ")
        return bstack11l11l1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦႸ")