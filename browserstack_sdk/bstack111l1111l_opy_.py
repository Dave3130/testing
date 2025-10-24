# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1l1l1l111_opy_():
  def __init__(self, args, logger, bstack1111l111_opy_, bstack111l1lll_opy_, bstack1111111ll1_opy_):
    self.args = args
    self.logger = logger
    self.bstack1111l111_opy_ = bstack1111l111_opy_
    self.bstack111l1lll_opy_ = bstack111l1lll_opy_
    self.bstack1111111ll1_opy_ = bstack1111111ll1_opy_
  def bstack1llll11l1_opy_(self, bstack1llllll11_opy_, bstack1lllll1l1_opy_, bstack1111111lll_opy_=False):
    bstack1111ll1l_opy_ = []
    manager = multiprocessing.Manager()
    bstack1lllllll1_opy_ = manager.list()
    bstack11111111_opy_ = Config.bstack1llll1ll1_opy_()
    if bstack1111111lll_opy_:
      for index, platform in enumerate(self.bstack1111l111_opy_[bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧႹ")]):
        if index == 0:
          bstack1lllll1l1_opy_[bstack11l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨႺ")] = self.args
        bstack1111ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1llllll11_opy_,
                                                    args=(bstack1lllll1l1_opy_, bstack1lllllll1_opy_)))
    else:
      for index, platform in enumerate(self.bstack1111l111_opy_[bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩႻ")]):
        bstack1111ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1llllll11_opy_,
                                                    args=(bstack1lllll1l1_opy_, bstack1lllllll1_opy_)))
    i = 0
    for t in bstack1111ll1l_opy_:
      try:
        if bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨႼ")):
          os.environ[bstack11l11l1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩႽ")] = json.dumps(self.bstack1111l111_opy_[bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬႾ")][i % self.bstack1111111ll1_opy_])
      except Exception as e:
        self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࡀࠠࡼࡿࠥႿ").format(str(e)))
      i += 1
      t.start()
    for t in bstack1111ll1l_opy_:
      t.join()
    return list(bstack1lllllll1_opy_)