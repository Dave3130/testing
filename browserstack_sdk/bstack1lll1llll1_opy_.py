# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11ll1l11l_opy_():
  def __init__(self, args, logger, bstack1lll11l1l_opy_, bstack1lll1l1ll_opy_, bstack1111111l11_opy_):
    self.args = args
    self.logger = logger
    self.bstack1lll11l1l_opy_ = bstack1lll11l1l_opy_
    self.bstack1lll1l1ll_opy_ = bstack1lll1l1ll_opy_
    self.bstack1111111l11_opy_ = bstack1111111l11_opy_
  def bstack1llllll11_opy_(self, bstack1lll1ll1l_opy_, bstack1lllll1ll_opy_, bstack11111111ll_opy_=False):
    bstack111ll111_opy_ = []
    manager = multiprocessing.Manager()
    bstack11111ll1_opy_ = manager.list()
    bstack111ll1l1_opy_ = Config.bstack111l1111_opy_()
    if bstack11111111ll_opy_:
      for index, platform in enumerate(self.bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫႽ")]):
        if index == 0:
          bstack1lllll1ll_opy_[bstack1lll11l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬႾ")] = self.args
        bstack111ll111_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll1ll1l_opy_,
                                                    args=(bstack1lllll1ll_opy_, bstack11111ll1_opy_)))
    else:
      for index, platform in enumerate(self.bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Ⴟ")]):
        bstack111ll111_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll1ll1l_opy_,
                                                    args=(bstack1lllll1ll_opy_, bstack11111ll1_opy_)))
    i = 0
    for t in bstack111ll111_opy_:
      try:
        if bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬჀ")):
          os.environ[bstack1lll11l_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭Ⴡ")] = json.dumps(self.bstack1lll11l1l_opy_[bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩჂ")][i % self.bstack1111111l11_opy_])
      except Exception as e:
        self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵ࠽ࠤࢀࢃࠢჃ").format(str(e)))
      i += 1
      t.start()
    for t in bstack111ll111_opy_:
      t.join()
    return list(bstack11111ll1_opy_)