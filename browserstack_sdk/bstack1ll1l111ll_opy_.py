# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1l111l11l_opy_():
  def __init__(self, args, logger, bstack1lll111l1_opy_, bstack111lll11_opy_, bstack11111111ll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1lll111l1_opy_ = bstack1lll111l1_opy_
    self.bstack111lll11_opy_ = bstack111lll11_opy_
    self.bstack11111111ll_opy_ = bstack11111111ll_opy_
  def bstack1lll1lll1_opy_(self, bstack1llll111l_opy_, bstack11111l1l_opy_, bstack1111111l11_opy_=False):
    bstack111l1ll1_opy_ = []
    manager = multiprocessing.Manager()
    bstack1111ll11_opy_ = manager.list()
    bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
    if bstack1111111l11_opy_:
      for index, platform in enumerate(self.bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫჄ")]):
        if index == 0:
          bstack11111l1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬჅ")] = self.args
        bstack111l1ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1llll111l_opy_,
                                                    args=(bstack11111l1l_opy_, bstack1111ll11_opy_)))
    else:
      for index, platform in enumerate(self.bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭჆")]):
        bstack111l1ll1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1llll111l_opy_,
                                                    args=(bstack11111l1l_opy_, bstack1111ll11_opy_)))
    i = 0
    for t in bstack111l1ll1_opy_:
      try:
        if bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬჇ")):
          os.environ[bstack1lllll1l_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭჈")] = json.dumps(self.bstack1lll111l1_opy_[bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ჉")][i % self.bstack11111111ll_opy_])
      except Exception as e:
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵ࠽ࠤࢀࢃࠢ჊").format(str(e)))
      i += 1
      t.start()
    for t in bstack111l1ll1_opy_:
      t.join()
    return list(bstack1111ll11_opy_)