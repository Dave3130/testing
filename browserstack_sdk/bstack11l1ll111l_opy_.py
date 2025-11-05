# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1ll11l11l_opy_():
  def __init__(self, args, logger, bstack1lll11l11_opy_, bstack1lll1l111_opy_, bstack1llllllllll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1lll11l11_opy_ = bstack1lll11l11_opy_
    self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
    self.bstack1llllllllll_opy_ = bstack1llllllllll_opy_
  def bstack11111ll1_opy_(self, bstack111ll1l1_opy_, bstack1llll1l1l_opy_, bstack1111111111_opy_=False):
    bstack1llll1l11_opy_ = []
    manager = multiprocessing.Manager()
    bstack1lll11l1l_opy_ = manager.list()
    bstack111lll11_opy_ = Config.bstack1111llll_opy_()
    if bstack1111111111_opy_:
      for index, platform in enumerate(self.bstack1lll11l11_opy_[bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩთ")]):
        if index == 0:
          bstack1llll1l1l_opy_[bstack11111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪი")] = self.args
        bstack1llll1l11_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111ll1l1_opy_,
                                                    args=(bstack1llll1l1l_opy_, bstack1lll11l1l_opy_)))
    else:
      for index, platform in enumerate(self.bstack1lll11l11_opy_[bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫკ")]):
        bstack1llll1l11_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111ll1l1_opy_,
                                                    args=(bstack1llll1l1l_opy_, bstack1lll11l1l_opy_)))
    i = 0
    for t in bstack1llll1l11_opy_:
      try:
        if bstack111lll11_opy_.get_property(bstack11111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪლ")):
          os.environ[bstack11111_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫმ")] = json.dumps(self.bstack1lll11l11_opy_[bstack11111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧნ")][i % self.bstack1llllllllll_opy_])
      except Exception as e:
        self.logger.debug(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠧო").format(str(e)))
      i += 1
      t.start()
    for t in bstack1llll1l11_opy_:
      t.join()
    return list(bstack1lll11l1l_opy_)