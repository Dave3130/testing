# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l1111ll_opy_():
  def __init__(self, args, logger, bstack111l11ll_opy_, bstack1lll1lll1_opy_, bstack111111lll1_opy_):
    self.args = args
    self.logger = logger
    self.bstack111l11ll_opy_ = bstack111l11ll_opy_
    self.bstack1lll1lll1_opy_ = bstack1lll1lll1_opy_
    self.bstack111111lll1_opy_ = bstack111111lll1_opy_
  def bstack1llllll11_opy_(self, bstack11l1l111_opy_, bstack111ll1ll_opy_, bstack111111ll1l_opy_=False):
    bstack11l11111_opy_ = []
    manager = multiprocessing.Manager()
    bstack111l11l1_opy_ = manager.list()
    bstack11111lll_opy_ = Config.bstack111l111l_opy_()
    if bstack111111ll1l_opy_:
      for index, platform in enumerate(self.bstack111l11ll_opy_[bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ႙")]):
        if index == 0:
          bstack111ll1ll_opy_[bstack111111l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫႚ")] = self.args
        bstack11l11111_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11l1l111_opy_,
                                                    args=(bstack111ll1ll_opy_, bstack111l11l1_opy_)))
    else:
      for index, platform in enumerate(self.bstack111l11ll_opy_[bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬႛ")]):
        bstack11l11111_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11l1l111_opy_,
                                                    args=(bstack111ll1ll_opy_, bstack111l11l1_opy_)))
    i = 0
    for t in bstack11l11111_opy_:
      try:
        if bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫႜ")):
          os.environ[bstack111111l_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬႝ")] = json.dumps(self.bstack111l11ll_opy_[bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ႞")][i % self.bstack111111lll1_opy_])
      except Exception as e:
        self.logger.debug(bstack111111l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡨࡸࡦ࡯࡬ࡴ࠼ࠣࡿࢂࠨ႟").format(str(e)))
      i += 1
      t.start()
    for t in bstack11l11111_opy_:
      t.join()
    return list(bstack111l11l1_opy_)