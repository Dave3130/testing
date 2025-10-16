# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1l1l11l1l1_opy_():
  def __init__(self, args, logger, bstack111l1l1l_opy_, bstack1111llll_opy_, bstack11111l1111_opy_):
    self.args = args
    self.logger = logger
    self.bstack111l1l1l_opy_ = bstack111l1l1l_opy_
    self.bstack1111llll_opy_ = bstack1111llll_opy_
    self.bstack11111l1111_opy_ = bstack11111l1111_opy_
  def bstack11l11ll1_opy_(self, bstack11l11lll_opy_, bstack1lllll1l1_opy_, bstack111111llll_opy_=False):
    bstack1111111l_opy_ = []
    manager = multiprocessing.Manager()
    bstack111llll1_opy_ = manager.list()
    bstack1lll1ll1l_opy_ = Config.bstack1llll11ll_opy_()
    if bstack111111llll_opy_:
      for index, platform in enumerate(self.bstack111l1l1l_opy_[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩႦ")]):
        if index == 0:
          bstack1lllll1l1_opy_[bstack1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪႧ")] = self.args
        bstack1111111l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11l11lll_opy_,
                                                    args=(bstack1lllll1l1_opy_, bstack111llll1_opy_)))
    else:
      for index, platform in enumerate(self.bstack111l1l1l_opy_[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫႨ")]):
        bstack1111111l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11l11lll_opy_,
                                                    args=(bstack1lllll1l1_opy_, bstack111llll1_opy_)))
    i = 0
    for t in bstack1111111l_opy_:
      try:
        if bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪႩ")):
          os.environ[bstack1l_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫႪ")] = json.dumps(self.bstack111l1l1l_opy_[bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧႫ")][i % self.bstack11111l1111_opy_])
      except Exception as e:
        self.logger.debug(bstack1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠧႬ").format(str(e)))
      i += 1
      t.start()
    for t in bstack1111111l_opy_:
      t.join()
    return list(bstack111llll1_opy_)