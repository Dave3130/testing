# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1ll1ll1l1_opy_():
  def __init__(self, args, logger, bstack1lll1lll1_opy_, bstack1lllll11l_opy_, bstack111111ll1l_opy_):
    self.args = args
    self.logger = logger
    self.bstack1lll1lll1_opy_ = bstack1lll1lll1_opy_
    self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
    self.bstack111111ll1l_opy_ = bstack111111ll1l_opy_
  def bstack1lllll1l1_opy_(self, bstack1llll1l11_opy_, bstack1llllll1l_opy_, bstack111111ll11_opy_=False):
    bstack111111l1_opy_ = []
    manager = multiprocessing.Manager()
    bstack1lll1ll11_opy_ = manager.list()
    bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
    if bstack111111ll11_opy_:
      for index, platform in enumerate(self.bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ႟")]):
        if index == 0:
          bstack1llllll1l_opy_[bstack1l1lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪႠ")] = self.args
        bstack111111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1llll1l11_opy_,
                                                    args=(bstack1llllll1l_opy_, bstack1lll1ll11_opy_)))
    else:
      for index, platform in enumerate(self.bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫႡ")]):
        bstack111111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1llll1l11_opy_,
                                                    args=(bstack1llllll1l_opy_, bstack1lll1ll11_opy_)))
    i = 0
    for t in bstack111111l1_opy_:
      try:
        if bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪႢ")):
          os.environ[bstack1l1lll1_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫႣ")] = json.dumps(self.bstack1lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧႤ")][i % self.bstack111111ll1l_opy_])
      except Exception as e:
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠧႥ").format(str(e)))
      i += 1
      t.start()
    for t in bstack111111l1_opy_:
      t.join()
    return list(bstack1lll1ll11_opy_)