# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack11l11l111l_opy_():
  def __init__(self, args, logger, bstack1llll1l1l_opy_, bstack1lll11ll1_opy_, bstack1111111111_opy_):
    self.args = args
    self.logger = logger
    self.bstack1llll1l1l_opy_ = bstack1llll1l1l_opy_
    self.bstack1lll11ll1_opy_ = bstack1lll11ll1_opy_
    self.bstack1111111111_opy_ = bstack1111111111_opy_
  def bstack1lll1l1l1_opy_(self, bstack1lllll11l_opy_, bstack111ll11l_opy_, bstack1llllllllll_opy_=False):
    bstack1lll1llll_opy_ = []
    manager = multiprocessing.Manager()
    bstack1llll1ll1_opy_ = manager.list()
    bstack111ll1l1_opy_ = Config.bstack111111ll_opy_()
    if bstack1llllllllll_opy_:
      for index, platform in enumerate(self.bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬდ")]):
        if index == 0:
          bstack111ll11l_opy_[bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ე")] = self.args
        bstack1lll1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lllll11l_opy_,
                                                    args=(bstack111ll11l_opy_, bstack1llll1ll1_opy_)))
    else:
      for index, platform in enumerate(self.bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧვ")]):
        bstack1lll1llll_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack1lllll11l_opy_,
                                                    args=(bstack111ll11l_opy_, bstack1llll1ll1_opy_)))
    i = 0
    for t in bstack1lll1llll_opy_:
      try:
        if bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ზ")):
          os.environ[bstack11ll1l_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧთ")] = json.dumps(self.bstack1llll1l1l_opy_[bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪი")][i % self.bstack1111111111_opy_])
      except Exception as e:
        self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡳࡵࡱࡵ࡭ࡳ࡭ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶ࠾ࠥࢁࡽࠣკ").format(str(e)))
      i += 1
      t.start()
    for t in bstack1lll1llll_opy_:
      t.join()
    return list(bstack1llll1ll1_opy_)