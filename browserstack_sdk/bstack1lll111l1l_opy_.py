# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1ll1l111l1_opy_():
  def __init__(self, args, logger, bstack11111l11_opy_, bstack1111l11l_opy_, bstack1111111lll_opy_):
    self.args = args
    self.logger = logger
    self.bstack11111l11_opy_ = bstack11111l11_opy_
    self.bstack1111l11l_opy_ = bstack1111l11l_opy_
    self.bstack1111111lll_opy_ = bstack1111111lll_opy_
  def bstack1lll11ll1_opy_(self, bstack111ll1l1_opy_, bstack1llllll1l_opy_, bstack1111111ll1_opy_=False):
    bstack111l1lll_opy_ = []
    manager = multiprocessing.Manager()
    bstack1llll11ll_opy_ = manager.list()
    bstack11l11111_opy_ = Config.bstack1111ll1l_opy_()
    if bstack1111111ll1_opy_:
      for index, platform in enumerate(self.bstack11111l11_opy_[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧႹ")]):
        if index == 0:
          bstack1llllll1l_opy_[bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨႺ")] = self.args
        bstack111l1lll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111ll1l1_opy_,
                                                    args=(bstack1llllll1l_opy_, bstack1llll11ll_opy_)))
    else:
      for index, platform in enumerate(self.bstack11111l11_opy_[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩႻ")]):
        bstack111l1lll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111ll1l1_opy_,
                                                    args=(bstack1llllll1l_opy_, bstack1llll11ll_opy_)))
    i = 0
    for t in bstack111l1lll_opy_:
      try:
        if bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨႼ")):
          os.environ[bstack1l1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩႽ")] = json.dumps(self.bstack11111l11_opy_[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬႾ")][i % self.bstack1111111lll_opy_])
      except Exception as e:
        self.logger.debug(bstack1l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࡀࠠࡼࡿࠥႿ").format(str(e)))
      i += 1
      t.start()
    for t in bstack111l1lll_opy_:
      t.join()
    return list(bstack1llll11ll_opy_)