# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l1lll111_opy_():
  def __init__(self, args, logger, bstack1lll111l1_opy_, bstack1lll1l111_opy_, bstack11111111l1_opy_):
    self.args = args
    self.logger = logger
    self.bstack1lll111l1_opy_ = bstack1lll111l1_opy_
    self.bstack1lll1l111_opy_ = bstack1lll1l111_opy_
    self.bstack11111111l1_opy_ = bstack11111111l1_opy_
  def bstack111l1lll_opy_(self, bstack1111l1l1_opy_, bstack1lllll1ll_opy_, bstack11111111ll_opy_=False):
    bstack1111lll1_opy_ = []
    manager = multiprocessing.Manager()
    bstack1lllllll1_opy_ = manager.list()
    bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
    if bstack11111111ll_opy_:
      for index, platform in enumerate(self.bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ჈")]):
        if index == 0:
          bstack1lllll1ll_opy_[bstack11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ჉")] = self.args
        bstack1111lll1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1111l1l1_opy_,
                                                    args=(bstack1lllll1ll_opy_, bstack1lllllll1_opy_)))
    else:
      for index, platform in enumerate(self.bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ჊")]):
        bstack1111lll1_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1111l1l1_opy_,
                                                    args=(bstack1lllll1ll_opy_, bstack1lllllll1_opy_)))
    i = 0
    for t in bstack1111lll1_opy_:
      try:
        if bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ჋")):
          os.environ[bstack11ll_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ჌")] = json.dumps(self.bstack1lll111l1_opy_[bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭Ⴭ")][i % self.bstack11111111l1_opy_])
      except Exception as e:
        self.logger.debug(bstack11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹ࠺ࠡࡽࢀࠦ჎").format(str(e)))
      i += 1
      t.start()
    for t in bstack1111lll1_opy_:
      t.join()
    return list(bstack1lllllll1_opy_)