# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11l1l111_opy_, bstack1lllll1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack11l1l111_opy_ = bstack11l1l111_opy_
        self.bstack1lllll1ll_opy_ = bstack1lllll1ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l111l1l_opy_(bstack11111l111l_opy_):
        bstack11111l11l1_opy_ = []
        if bstack11111l111l_opy_:
            tokens = str(os.path.basename(bstack11111l111l_opy_)).split(bstack1lllll1_opy_ (u"ࠨ࡟ࠣ႟"))
            camelcase_name = bstack1lllll1_opy_ (u"ࠢࠡࠤႠ").join(t.title() for t in tokens)
            suite_name, bstack11111l1l11_opy_ = os.path.splitext(camelcase_name)
            bstack11111l11l1_opy_.append(suite_name)
        return bstack11111l11l1_opy_
    @staticmethod
    def bstack11111l11ll_opy_(typename):
        if bstack1lllll1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦႡ") in typename:
            return bstack1lllll1_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥႢ")
        return bstack1lllll1_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦႣ")