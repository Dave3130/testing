# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack1111l1ll_opy_, bstack1llll111l_opy_):
        self.args = args
        self.logger = logger
        self.bstack1111l1ll_opy_ = bstack1111l1ll_opy_
        self.bstack1llll111l_opy_ = bstack1llll111l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1ll1111l_opy_(bstack1111111l11_opy_):
        bstack1111111ll1_opy_ = []
        if bstack1111111l11_opy_:
            tokens = str(os.path.basename(bstack1111111l11_opy_)).split(bstack11l1l11_opy_ (u"ࠨ࡟ࠣႻ"))
            camelcase_name = bstack11l1l11_opy_ (u"ࠢࠡࠤႼ").join(t.title() for t in tokens)
            suite_name, bstack1111111lll_opy_ = os.path.splitext(camelcase_name)
            bstack1111111ll1_opy_.append(suite_name)
        return bstack1111111ll1_opy_
    @staticmethod
    def bstack1111111l1l_opy_(typename):
        if bstack11l1l11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦႽ") in typename:
            return bstack11l1l11_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࡊࡸࡲࡰࡴࠥႾ")
        return bstack11l1l11_opy_ (u"࡙ࠥࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠦႿ")