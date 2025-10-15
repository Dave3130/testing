# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1l11ll1l11_opy_():
  def __init__(self, args, logger, bstack111l1111_opy_, bstack111ll1ll_opy_, bstack111111lll1_opy_):
    self.args = args
    self.logger = logger
    self.bstack111l1111_opy_ = bstack111l1111_opy_
    self.bstack111ll1ll_opy_ = bstack111ll1ll_opy_
    self.bstack111111lll1_opy_ = bstack111111lll1_opy_
  def bstack1llll1lll_opy_(self, bstack1111l11l_opy_, bstack1111111l_opy_, bstack111111ll1l_opy_=False):
    bstack1llll1l1l_opy_ = []
    manager = multiprocessing.Manager()
    bstack11l1l11l_opy_ = manager.list()
    bstack111111ll_opy_ = Config.bstack111l1ll1_opy_()
    if bstack111111ll1l_opy_:
      for index, platform in enumerate(self.bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ႞")]):
        if index == 0:
          bstack1111111l_opy_[bstack1ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ႟")] = self.args
        bstack1llll1l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1111l11l_opy_,
                                                    args=(bstack1111111l_opy_, bstack11l1l11l_opy_)))
    else:
      for index, platform in enumerate(self.bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪႠ")]):
        bstack1llll1l1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1111l11l_opy_,
                                                    args=(bstack1111111l_opy_, bstack11l1l11l_opy_)))
    i = 0
    for t in bstack1llll1l1l_opy_:
      try:
        if bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩႡ")):
          os.environ[bstack1ll1l_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪႢ")] = json.dumps(self.bstack111l1111_opy_[bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Ⴃ")][i % self.bstack111111lll1_opy_])
      except Exception as e:
        self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹ࠺ࠡࡽࢀࠦႤ").format(str(e)))
      i += 1
      t.start()
    for t in bstack1llll1l1l_opy_:
      t.join()
    return list(bstack11l1l11l_opy_)