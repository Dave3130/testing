# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1l1ll1l11l_opy_():
  def __init__(self, args, logger, bstack111l1lll_opy_, bstack1lll1ll1l_opy_, bstack11111111ll_opy_):
    self.args = args
    self.logger = logger
    self.bstack111l1lll_opy_ = bstack111l1lll_opy_
    self.bstack1lll1ll1l_opy_ = bstack1lll1ll1l_opy_
    self.bstack11111111ll_opy_ = bstack11111111ll_opy_
  def bstack1lll11lll_opy_(self, bstack1llll1ll1_opy_, bstack1llll1111_opy_, bstack1111111l11_opy_=False):
    bstack111lll1l_opy_ = []
    manager = multiprocessing.Manager()
    bstack1lll111ll_opy_ = manager.list()
    bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
    if bstack1111111l11_opy_:
      for index, platform in enumerate(self.bstack111l1lll_opy_[bstack11lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧჀ")]):
        if index == 0:
          bstack1llll1111_opy_[bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨჁ")] = self.args
        bstack111lll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1llll1ll1_opy_,
                                                    args=(bstack1llll1111_opy_, bstack1lll111ll_opy_)))
    else:
      for index, platform in enumerate(self.bstack111l1lll_opy_[bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩჂ")]):
        bstack111lll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1llll1ll1_opy_,
                                                    args=(bstack1llll1111_opy_, bstack1lll111ll_opy_)))
    i = 0
    for t in bstack111lll1l_opy_:
      try:
        if bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨჃ")):
          os.environ[bstack11lll1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩჄ")] = json.dumps(self.bstack111l1lll_opy_[bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬჅ")][i % self.bstack11111111ll_opy_])
      except Exception as e:
        self.logger.debug(bstack11lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࡀࠠࡼࡿࠥ჆").format(str(e)))
      i += 1
      t.start()
    for t in bstack111lll1l_opy_:
      t.join()
    return list(bstack1lll111ll_opy_)