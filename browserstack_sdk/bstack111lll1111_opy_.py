# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1ll111l11l_opy_():
  def __init__(self, args, logger, bstack1lllll11l_opy_, bstack111ll1ll_opy_, bstack111111ll11_opy_):
    self.args = args
    self.logger = logger
    self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
    self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
    self.bstack111111ll11_opy_ = bstack111111ll11_opy_
  def bstack111lll1l_opy_(self, bstack1111111l_opy_, bstack111l1111_opy_, bstack111111ll1l_opy_=False):
    bstack111lllll_opy_ = []
    manager = multiprocessing.Manager()
    bstack11l1l11l_opy_ = manager.list()
    bstack11l1111l_opy_ = Config.bstack111111ll_opy_()
    if bstack111111ll1l_opy_:
      for index, platform in enumerate(self.bstack1lllll11l_opy_[bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ႓")]):
        if index == 0:
          bstack111l1111_opy_[bstack11111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ႔")] = self.args
        bstack111lllll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1111111l_opy_,
                                                    args=(bstack111l1111_opy_, bstack11l1l11l_opy_)))
    else:
      for index, platform in enumerate(self.bstack1lllll11l_opy_[bstack11111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭႕")]):
        bstack111lllll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1111111l_opy_,
                                                    args=(bstack111l1111_opy_, bstack11l1l11l_opy_)))
    i = 0
    for t in bstack111lllll_opy_:
      try:
        if bstack11l1111l_opy_.get_property(bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ႖")):
          os.environ[bstack11111_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭႗")] = json.dumps(self.bstack1lllll11l_opy_[bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ႘")][i % self.bstack111111ll11_opy_])
      except Exception as e:
        self.logger.debug(bstack11111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵ࠽ࠤࢀࢃࠢ႙").format(str(e)))
      i += 1
      t.start()
    for t in bstack111lllll_opy_:
      t.join()
    return list(bstack11l1l11l_opy_)