# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack111l11ll_opy_, bstack1lll1lll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack111l11ll_opy_ = bstack111l11ll_opy_
        self.bstack1lll1lll1_opy_ = bstack1lll1lll1_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1ll1l1_opy_(bstack11111l1111_opy_):
        bstack11111l11l1_opy_ = []
        if bstack11111l1111_opy_:
            tokens = str(os.path.basename(bstack11111l1111_opy_)).split(bstack111111l_opy_ (u"ࠤࡢࠦ႔"))
            camelcase_name = bstack111111l_opy_ (u"ࠥࠤࠧ႕").join(t.title() for t in tokens)
            suite_name, bstack111111llll_opy_ = os.path.splitext(camelcase_name)
            bstack11111l11l1_opy_.append(suite_name)
        return bstack11111l11l1_opy_
    @staticmethod
    def bstack11111l111l_opy_(typename):
        if bstack111111l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢ႖") in typename:
            return bstack111111l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨ႗")
        return bstack111111l_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢ႘")