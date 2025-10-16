# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l1ll1ll_opy_():
  def __init__(self, args, logger, bstack11l1l111_opy_, bstack1lllll1ll_opy_, bstack11111l1111_opy_):
    self.args = args
    self.logger = logger
    self.bstack11l1l111_opy_ = bstack11l1l111_opy_
    self.bstack1lllll1ll_opy_ = bstack1lllll1ll_opy_
    self.bstack11111l1111_opy_ = bstack11111l1111_opy_
  def bstack11l11l1l_opy_(self, bstack1lllll111_opy_, bstack111l1111_opy_, bstack111111llll_opy_=False):
    bstack111l1lll_opy_ = []
    manager = multiprocessing.Manager()
    bstack111lllll_opy_ = manager.list()
    bstack11l1111l_opy_ = Config.bstack11111l1l_opy_()
    if bstack111111llll_opy_:
      for index, platform in enumerate(self.bstack11l1l111_opy_[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧႤ")]):
        if index == 0:
          bstack111l1111_opy_[bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨႥ")] = self.args
        bstack111l1lll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lllll111_opy_,
                                                    args=(bstack111l1111_opy_, bstack111lllll_opy_)))
    else:
      for index, platform in enumerate(self.bstack11l1l111_opy_[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩႦ")]):
        bstack111l1lll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lllll111_opy_,
                                                    args=(bstack111l1111_opy_, bstack111lllll_opy_)))
    i = 0
    for t in bstack111l1lll_opy_:
      try:
        if bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨႧ")):
          os.environ[bstack1lllll1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩႨ")] = json.dumps(self.bstack11l1l111_opy_[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬႩ")][i % self.bstack11111l1111_opy_])
      except Exception as e:
        self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࡀࠠࡼࡿࠥႪ").format(str(e)))
      i += 1
      t.start()
    for t in bstack111l1lll_opy_:
      t.join()
    return list(bstack111lllll_opy_)