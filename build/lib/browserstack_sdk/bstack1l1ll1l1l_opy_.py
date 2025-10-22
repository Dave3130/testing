# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11111l1111_opy_():
  def __init__(self, args, logger, bstack1lll1l111_opy_, bstack1lll11l11_opy_, bstack11111111ll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
    self.bstack1lll11l11_opy_ = bstack1lll11l11_opy_
    self.bstack11111111ll_opy_ = bstack11111111ll_opy_
  def bstack111l111l_opy_(self, bstack1lll1l11l_opy_, bstack11111lll_opy_, bstack11111111l1_opy_=False):
    bstack1llll111l_opy_ = []
    manager = multiprocessing.Manager()
    bstack111l1l1l_opy_ = manager.list()
    bstack111l11ll_opy_ = Config.bstack111l11l1_opy_()
    if bstack11111111l1_opy_:
      for index, platform in enumerate(self.bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨჁ")]):
        if index == 0:
          bstack11111lll_opy_[bstack1l111ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩჂ")] = self.args
        bstack1llll111l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll1l11l_opy_,
                                                    args=(bstack11111lll_opy_, bstack111l1l1l_opy_)))
    else:
      for index, platform in enumerate(self.bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪჃ")]):
        bstack1llll111l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll1l11l_opy_,
                                                    args=(bstack11111lll_opy_, bstack111l1l1l_opy_)))
    i = 0
    for t in bstack1llll111l_opy_:
      try:
        if bstack111l11ll_opy_.get_property(bstack1l111ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩჄ")):
          os.environ[bstack1l111ll_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪჅ")] = json.dumps(self.bstack1lll1l111_opy_[bstack1l111ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭჆")][i % self.bstack11111111ll_opy_])
      except Exception as e:
        self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹ࠺ࠡࡽࢀࠦჇ").format(str(e)))
      i += 1
      t.start()
    for t in bstack1llll111l_opy_:
      t.join()
    return list(bstack111l1l1l_opy_)