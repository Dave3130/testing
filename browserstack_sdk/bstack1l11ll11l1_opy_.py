# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l1111l11_opy_():
  def __init__(self, args, logger, bstack111ll1ll_opy_, bstack111l1l1l_opy_, bstack111111lll1_opy_):
    self.args = args
    self.logger = logger
    self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
    self.bstack111l1l1l_opy_ = bstack111l1l1l_opy_
    self.bstack111111lll1_opy_ = bstack111111lll1_opy_
  def bstack1llll11ll_opy_(self, bstack11111lll_opy_, bstack1llllll11_opy_, bstack111111ll1l_opy_=False):
    bstack1lll1llll_opy_ = []
    manager = multiprocessing.Manager()
    bstack111ll1l1_opy_ = manager.list()
    bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
    if bstack111111ll1l_opy_:
      for index, platform in enumerate(self.bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ႜ")]):
        if index == 0:
          bstack1llllll11_opy_[bstack11l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧႝ")] = self.args
        bstack1lll1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111lll_opy_,
                                                    args=(bstack1llllll11_opy_, bstack111ll1l1_opy_)))
    else:
      for index, platform in enumerate(self.bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ႞")]):
        bstack1lll1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111lll_opy_,
                                                    args=(bstack1llllll11_opy_, bstack111ll1l1_opy_)))
    i = 0
    for t in bstack1lll1llll_opy_:
      try:
        if bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ႟")):
          os.environ[bstack11l1l11_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨႠ")] = json.dumps(self.bstack111ll1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫႡ")][i % self.bstack111111lll1_opy_])
      except Exception as e:
        self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡶࡲࡶ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠿ࠦࡻࡾࠤႢ").format(str(e)))
      i += 1
      t.start()
    for t in bstack1lll1llll_opy_:
      t.join()
    return list(bstack111ll1l1_opy_)