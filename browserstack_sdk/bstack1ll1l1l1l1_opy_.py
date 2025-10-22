# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack111ll11ll_opy_():
  def __init__(self, args, logger, bstack1111l1ll_opy_, bstack1llll111l_opy_, bstack11111111ll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1111l1ll_opy_ = bstack1111l1ll_opy_
    self.bstack1llll111l_opy_ = bstack1llll111l_opy_
    self.bstack11111111ll_opy_ = bstack11111111ll_opy_
  def bstack11111l1l_opy_(self, bstack11111111_opy_, bstack1llll1l1l_opy_, bstack11111111l1_opy_=False):
    bstack1lll111l1_opy_ = []
    manager = multiprocessing.Manager()
    bstack1111l11l_opy_ = manager.list()
    bstack111ll1ll_opy_ = Config.bstack1llll1lll_opy_()
    if bstack11111111l1_opy_:
      for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧჀ")]):
        if index == 0:
          bstack1llll1l1l_opy_[bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨჁ")] = self.args
        bstack1lll111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111111_opy_,
                                                    args=(bstack1llll1l1l_opy_, bstack1111l11l_opy_)))
    else:
      for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩჂ")]):
        bstack1lll111l1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111111_opy_,
                                                    args=(bstack1llll1l1l_opy_, bstack1111l11l_opy_)))
    i = 0
    for t in bstack1lll111l1_opy_:
      try:
        if bstack111ll1ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨჃ")):
          os.environ[bstack11l1l11_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩჄ")] = json.dumps(self.bstack1111l1ll_opy_[bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬჅ")][i % self.bstack11111111ll_opy_])
      except Exception as e:
        self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡷࡳࡷ࡯࡮ࡨࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࡀࠠࡼࡿࠥ჆").format(str(e)))
      i += 1
      t.start()
    for t in bstack1lll111l1_opy_:
      t.join()
    return list(bstack1111l11l_opy_)