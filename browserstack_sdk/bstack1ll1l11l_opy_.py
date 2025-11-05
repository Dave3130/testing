# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
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
    def bstack1l111111_opy_(bstack111111111l_opy_):
        bstack11111111ll_opy_ = []
        if bstack111111111l_opy_:
            tokens = str(os.path.basename(bstack111111111l_opy_)).split(bstack11ll1ll_opy_ (u"ࠤࡢࠦდ"))
            camelcase_name = bstack11ll1ll_opy_ (u"ࠥࠤࠧე").join(t.title() for t in tokens)
            suite_name, bstack11111111l1_opy_ = os.path.splitext(camelcase_name)
            bstack11111111ll_opy_.append(suite_name)
        return bstack11111111ll_opy_
    @staticmethod
    def bstack1111111l11_opy_(typename):
        if bstack11ll1ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢვ") in typename:
            return bstack11ll1ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨზ")
        return bstack11ll1ll_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢთ")