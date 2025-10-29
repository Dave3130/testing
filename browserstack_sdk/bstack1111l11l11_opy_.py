# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l1llll11_opy_():
  def __init__(self, args, logger, bstack1llllllll_opy_, bstack1llll1111_opy_, bstack1llllllllll_opy_):
    self.args = args
    self.logger = logger
    self.bstack1llllllll_opy_ = bstack1llllllll_opy_
    self.bstack1llll1111_opy_ = bstack1llll1111_opy_
    self.bstack1llllllllll_opy_ = bstack1llllllllll_opy_
  def bstack1lll11lll_opy_(self, bstack111l1lll_opy_, bstack1lll1l1ll_opy_, bstack1111111111_opy_=False):
    bstack111l11ll_opy_ = []
    manager = multiprocessing.Manager()
    bstack1111ll11_opy_ = manager.list()
    bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
    if bstack1111111111_opy_:
      for index, platform in enumerate(self.bstack1llllllll_opy_[bstack11l11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬდ")]):
        if index == 0:
          bstack1lll1l1ll_opy_[bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ე")] = self.args
        bstack111l11ll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111l1lll_opy_,
                                                    args=(bstack1lll1l1ll_opy_, bstack1111ll11_opy_)))
    else:
      for index, platform in enumerate(self.bstack1llllllll_opy_[bstack11l11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧვ")]):
        bstack111l11ll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack111l1lll_opy_,
                                                    args=(bstack1lll1l1ll_opy_, bstack1111ll11_opy_)))
    i = 0
    for t in bstack111l11ll_opy_:
      try:
        if bstack1lll11111_opy_.get_property(bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ზ")):
          os.environ[bstack11l11ll_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧთ")] = json.dumps(self.bstack1llllllll_opy_[bstack11l11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪი")][i % self.bstack1llllllllll_opy_])
      except Exception as e:
        self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡳࡵࡱࡵ࡭ࡳ࡭ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶ࠾ࠥࢁࡽࠣკ").format(str(e)))
      i += 1
      t.start()
    for t in bstack111l11ll_opy_:
      t.join()
    return list(bstack1111ll11_opy_)