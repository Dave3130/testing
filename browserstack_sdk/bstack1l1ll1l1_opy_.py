# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11l111ll_opy_, bstack11l11ll1_opy_):
        self.args = args
        self.logger = logger
        self.bstack11l111ll_opy_ = bstack11l111ll_opy_
        self.bstack11l11ll1_opy_ = bstack11l11ll1_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1l1ll1_opy_(bstack11111l11l1_opy_):
        bstack11111l1l11_opy_ = []
        if bstack11111l11l1_opy_:
            tokens = str(os.path.basename(bstack11111l11l1_opy_)).split(bstack1ll11_opy_ (u"ࠧࡥࠢ႞"))
            camelcase_name = bstack1ll11_opy_ (u"ࠨࠠࠣ႟").join(t.title() for t in tokens)
            suite_name, bstack11111l11ll_opy_ = os.path.splitext(camelcase_name)
            bstack11111l1l11_opy_.append(suite_name)
        return bstack11111l1l11_opy_
    @staticmethod
    def bstack11111l111l_opy_(typename):
        if bstack1ll11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥႠ") in typename:
            return bstack1ll11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤႡ")
        return bstack1ll11_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥႢ")