# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l1l1111_opy_():
  def __init__(self, args, logger, bstack1llll1l1l_opy_, bstack1lll1llll_opy_, bstack11111111ll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1llll1l1l_opy_ = bstack1llll1l1l_opy_
    self.bstack1lll1llll_opy_ = bstack1lll1llll_opy_
    self.bstack11111111ll_opy_ = bstack11111111ll_opy_
  def bstack1llll1ll1_opy_(self, bstack1lll11ll1_opy_, bstack111111l1_opy_, bstack1111111l11_opy_=False):
    bstack1llll1111_opy_ = []
    manager = multiprocessing.Manager()
    bstack1lll11l1l_opy_ = manager.list()
    bstack11111l11_opy_ = Config.bstack111l11l1_opy_()
    if bstack1111111l11_opy_:
      for index, platform in enumerate(self.bstack1llll1l1l_opy_[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭჆")]):
        if index == 0:
          bstack111111l1_opy_[bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧჇ")] = self.args
        bstack1llll1111_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll11ll1_opy_,
                                                    args=(bstack111111l1_opy_, bstack1lll11l1l_opy_)))
    else:
      for index, platform in enumerate(self.bstack1llll1l1l_opy_[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ჈")]):
        bstack1llll1111_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll11ll1_opy_,
                                                    args=(bstack111111l1_opy_, bstack1lll11l1l_opy_)))
    i = 0
    for t in bstack1llll1111_opy_:
      try:
        if bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ჉")):
          os.environ[bstack11l111_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ჊")] = json.dumps(self.bstack1llll1l1l_opy_[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ჋")][i % self.bstack11111111ll_opy_])
      except Exception as e:
        self.logger.debug(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡶࡲࡶ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠿ࠦࡻࡾࠤ჌").format(str(e)))
      i += 1
      t.start()
    for t in bstack1llll1111_opy_:
      t.join()
    return list(bstack1lll11l1l_opy_)