# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack111lllll11_opy_():
  def __init__(self, args, logger, bstack11l111ll_opy_, bstack11l11ll1_opy_, bstack111111llll_opy_):
    self.args = args
    self.logger = logger
    self.bstack11l111ll_opy_ = bstack11l111ll_opy_
    self.bstack11l11ll1_opy_ = bstack11l11ll1_opy_
    self.bstack111111llll_opy_ = bstack111111llll_opy_
  def bstack1llll1lll_opy_(self, bstack111llll1_opy_, bstack11111ll1_opy_, bstack11111l1111_opy_=False):
    bstack11l1111l_opy_ = []
    manager = multiprocessing.Manager()
    bstack111l1l11_opy_ = manager.list()
    bstack1111ll11_opy_ = Config.bstack1llll11l1_opy_()
    if bstack11111l1111_opy_:
      for index, platform in enumerate(self.bstack11l111ll_opy_[bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Ⴃ")]):
        if index == 0:
          bstack11111ll1_opy_[bstack1ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧႤ")] = self.args
        bstack11l1111l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111llll1_opy_,
                                                    args=(bstack11111ll1_opy_, bstack111l1l11_opy_)))
    else:
      for index, platform in enumerate(self.bstack11l111ll_opy_[bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨႥ")]):
        bstack11l1111l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111llll1_opy_,
                                                    args=(bstack11111ll1_opy_, bstack111l1l11_opy_)))
    i = 0
    for t in bstack11l1111l_opy_:
      try:
        if bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧႦ")):
          os.environ[bstack1ll11_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨႧ")] = json.dumps(self.bstack11l111ll_opy_[bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫႨ")][i % self.bstack111111llll_opy_])
      except Exception as e:
        self.logger.debug(bstack1ll11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡶࡲࡶ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠿ࠦࡻࡾࠤႩ").format(str(e)))
      i += 1
      t.start()
    for t in bstack11l1111l_opy_:
      t.join()
    return list(bstack111l1l11_opy_)