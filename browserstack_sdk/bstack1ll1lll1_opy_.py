# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
class RobotHandler():
    def __init__(self, args, logger, bstack111ll1ll_opy_, bstack111l1l1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
        self.bstack111l1l1l_opy_ = bstack111l1l1l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l1l1l1l_opy_(bstack11111l11l1_opy_):
        bstack11111l1111_opy_ = []
        if bstack11111l11l1_opy_:
            tokens = str(os.path.basename(bstack11111l11l1_opy_)).split(bstack11l1l11_opy_ (u"ࠧࡥࠢ႗"))
            camelcase_name = bstack11l1l11_opy_ (u"ࠨࠠࠣ႘").join(t.title() for t in tokens)
            suite_name, bstack111111llll_opy_ = os.path.splitext(camelcase_name)
            bstack11111l1111_opy_.append(suite_name)
        return bstack11111l1111_opy_
    @staticmethod
    def bstack11111l111l_opy_(typename):
        if bstack11l1l11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ႙") in typename:
            return bstack11l1l11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤႚ")
        return bstack11l1l11_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥႛ")