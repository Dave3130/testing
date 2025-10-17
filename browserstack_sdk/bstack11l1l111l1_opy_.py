# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l1lll1l1_opy_():
  def __init__(self, args, logger, bstack1lllll11l_opy_, bstack11l1l11l_opy_, bstack111111l1ll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1lllll11l_opy_ = bstack1lllll11l_opy_
    self.bstack11l1l11l_opy_ = bstack11l1l11l_opy_
    self.bstack111111l1ll_opy_ = bstack111111l1ll_opy_
  def bstack11111l1l_opy_(self, bstack111111l1_opy_, bstack111l1111_opy_, bstack111111ll11_opy_=False):
    bstack1111l1ll_opy_ = []
    manager = multiprocessing.Manager()
    bstack11l1111l_opy_ = manager.list()
    bstack111ll111_opy_ = Config.bstack111ll1ll_opy_()
    if bstack111111ll11_opy_:
      for index, platform in enumerate(self.bstack1lllll11l_opy_[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ႓")]):
        if index == 0:
          bstack111l1111_opy_[bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ႔")] = self.args
        bstack1111l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111111l1_opy_,
                                                    args=(bstack111l1111_opy_, bstack11l1111l_opy_)))
    else:
      for index, platform in enumerate(self.bstack1lllll11l_opy_[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭႕")]):
        bstack1111l1ll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111111l1_opy_,
                                                    args=(bstack111l1111_opy_, bstack11l1111l_opy_)))
    i = 0
    for t in bstack1111l1ll_opy_:
      try:
        if bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ႖")):
          os.environ[bstack11l111_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭႗")] = json.dumps(self.bstack1lllll11l_opy_[bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ႘")][i % self.bstack111111l1ll_opy_])
      except Exception as e:
        self.logger.debug(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵ࠽ࠤࢀࢃࠢ႙").format(str(e)))
      i += 1
      t.start()
    for t in bstack1111l1ll_opy_:
      t.join()
    return list(bstack11l1111l_opy_)