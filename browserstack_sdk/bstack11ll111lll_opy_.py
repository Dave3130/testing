# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1l11llll1l_opy_():
  def __init__(self, args, logger, bstack11111l11_opy_, bstack1lll111ll_opy_, bstack11111111ll_opy_):
    self.args = args
    self.logger = logger
    self.bstack11111l11_opy_ = bstack11111l11_opy_
    self.bstack1lll111ll_opy_ = bstack1lll111ll_opy_
    self.bstack11111111ll_opy_ = bstack11111111ll_opy_
  def bstack1lllllll1_opy_(self, bstack1lll1l11l_opy_, bstack111l111l_opy_, bstack11111111l1_opy_=False):
    bstack1llll11ll_opy_ = []
    manager = multiprocessing.Manager()
    bstack1111l11l_opy_ = manager.list()
    bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
    if bstack11111111l1_opy_:
      for index, platform in enumerate(self.bstack11111l11_opy_[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨჁ")]):
        if index == 0:
          bstack111l111l_opy_[bstack111l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩჂ")] = self.args
        bstack1llll11ll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll1l11l_opy_,
                                                    args=(bstack111l111l_opy_, bstack1111l11l_opy_)))
    else:
      for index, platform in enumerate(self.bstack11111l11_opy_[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪჃ")]):
        bstack1llll11ll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lll1l11l_opy_,
                                                    args=(bstack111l111l_opy_, bstack1111l11l_opy_)))
    i = 0
    for t in bstack1llll11ll_opy_:
      try:
        if bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩჄ")):
          os.environ[bstack111l1l_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪჅ")] = json.dumps(self.bstack11111l11_opy_[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭჆")][i % self.bstack11111111ll_opy_])
      except Exception as e:
        self.logger.debug(bstack111l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹ࠺ࠡࡽࢀࠦჇ").format(str(e)))
      i += 1
      t.start()
    for t in bstack1llll11ll_opy_:
      t.join()
    return list(bstack1111l11l_opy_)