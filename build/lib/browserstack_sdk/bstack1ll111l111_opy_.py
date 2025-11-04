# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack111ll1l11l_opy_():
  def __init__(self, args, logger, bstack111ll11l_opy_, bstack1lll1l1l1_opy_, bstack1111111111_opy_):
    self.args = args
    self.logger = logger
    self.bstack111ll11l_opy_ = bstack111ll11l_opy_
    self.bstack1lll1l1l1_opy_ = bstack1lll1l1l1_opy_
    self.bstack1111111111_opy_ = bstack1111111111_opy_
  def bstack1lll11lll_opy_(self, bstack1lll11l11_opy_, bstack1111ll1l_opy_, bstack1llllllllll_opy_=False):
    bstack1lll111l1_opy_ = []
    manager = multiprocessing.Manager()
    bstack11111lll_opy_ = manager.list()
    bstack1llll11ll_opy_ = Config.bstack1llllllll_opy_()
    if bstack1llllllllll_opy_:
      for index, platform in enumerate(self.bstack111ll11l_opy_[bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩთ")]):
        if index == 0:
          bstack1111ll1l_opy_[bstack11l1111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪი")] = self.args
        bstack1lll111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll11l11_opy_,
                                                    args=(bstack1111ll1l_opy_, bstack11111lll_opy_)))
    else:
      for index, platform in enumerate(self.bstack111ll11l_opy_[bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫკ")]):
        bstack1lll111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll11l11_opy_,
                                                    args=(bstack1111ll1l_opy_, bstack11111lll_opy_)))
    i = 0
    for t in bstack1lll111l1_opy_:
      try:
        if bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪლ")):
          os.environ[bstack11l1111_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫმ")] = json.dumps(self.bstack111ll11l_opy_[bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧნ")][i % self.bstack1111111111_opy_])
      except Exception as e:
        self.logger.debug(bstack11l1111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠧო").format(str(e)))
      i += 1
      t.start()
    for t in bstack1lll111l1_opy_:
      t.join()
    return list(bstack11111lll_opy_)