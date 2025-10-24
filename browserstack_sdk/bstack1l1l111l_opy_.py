# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11111l11_opy_, bstack1111l11l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11111l11_opy_ = bstack11111l11_opy_
        self.bstack1111l11l_opy_ = bstack1111l11l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1ll11l11_opy_(bstack111111l1l1_opy_):
        bstack111111l1ll_opy_ = []
        if bstack111111l1l1_opy_:
            tokens = str(os.path.basename(bstack111111l1l1_opy_)).split(bstack1l1_opy_ (u"ࠨ࡟ࠣႴ"))
            camelcase_name = bstack1l1_opy_ (u"ࠢࠡࠤႵ").join(t.title() for t in tokens)
            suite_name, bstack111111l11l_opy_ = os.path.splitext(camelcase_name)
            bstack111111l1ll_opy_.append(suite_name)
        return bstack111111l1ll_opy_
    @staticmethod
    def bstack111111l111_opy_(typename):
        if bstack1l1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦႶ") in typename:
            return bstack1l1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥႷ")
        return bstack1l1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦႸ")