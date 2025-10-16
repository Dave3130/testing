# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack111lll1l11_opy_():
  def __init__(self, args, logger, bstack1111l1ll_opy_, bstack111l11ll_opy_, bstack111111llll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1111l1ll_opy_ = bstack1111l1ll_opy_
    self.bstack111l11ll_opy_ = bstack111l11ll_opy_
    self.bstack111111llll_opy_ = bstack111111llll_opy_
  def bstack111llll1_opy_(self, bstack111ll11l_opy_, bstack1111lll1_opy_, bstack11111l1111_opy_=False):
    bstack111lll11_opy_ = []
    manager = multiprocessing.Manager()
    bstack11l111ll_opy_ = manager.list()
    bstack11111l11_opy_ = Config.bstack1llllllll_opy_()
    if bstack11111l1111_opy_:
      for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨႥ")]):
        if index == 0:
          bstack1111lll1_opy_[bstack1ll1ll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩႦ")] = self.args
        bstack111lll11_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111ll11l_opy_,
                                                    args=(bstack1111lll1_opy_, bstack11l111ll_opy_)))
    else:
      for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪႧ")]):
        bstack111lll11_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111ll11l_opy_,
                                                    args=(bstack1111lll1_opy_, bstack11l111ll_opy_)))
    i = 0
    for t in bstack111lll11_opy_:
      try:
        if bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩႨ")):
          os.environ[bstack1ll1ll1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪႩ")] = json.dumps(self.bstack1111l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Ⴊ")][i % self.bstack111111llll_opy_])
      except Exception as e:
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹ࠺ࠡࡽࢀࠦႫ").format(str(e)))
      i += 1
      t.start()
    for t in bstack111lll11_opy_:
      t.join()
    return list(bstack11l111ll_opy_)