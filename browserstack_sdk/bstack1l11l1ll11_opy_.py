# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import json
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1l11llllll_opy_():
  def __init__(self, args, logger, bstack1111l1ll_opy_, bstack1llll111l_opy_, bstack1111111111_opy_):
    self.args = args
    self.logger = logger
    self.bstack1111l1ll_opy_ = bstack1111l1ll_opy_
    self.bstack1llll111l_opy_ = bstack1llll111l_opy_
    self.bstack1111111111_opy_ = bstack1111111111_opy_
  def bstack1lllll111_opy_(self, bstack11111l1l_opy_, bstack1lll11l1l_opy_, bstack1llllllllll_opy_=False):
    bstack11111l11_opy_ = []
    manager = multiprocessing.Manager()
    bstack1llll1lll_opy_ = manager.list()
    bstack1llllll1l_opy_ = Config.bstack1lll11ll1_opy_()
    if bstack1llllllllll_opy_:
      for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪი")]):
        if index == 0:
          bstack1lll11l1l_opy_[bstack11ll1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫკ")] = self.args
        bstack11111l11_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111l1l_opy_,
                                                    args=(bstack1lll11l1l_opy_, bstack1llll1lll_opy_)))
    else:
      for index, platform in enumerate(self.bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬლ")]):
        bstack11111l11_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111l1l_opy_,
                                                    args=(bstack1lll11l1l_opy_, bstack1llll1lll_opy_)))
    i = 0
    for t in bstack11111l11_opy_:
      try:
        if bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫმ")):
          os.environ[bstack11ll1ll_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬნ")] = json.dumps(self.bstack1111l1ll_opy_[bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨო")][i % self.bstack1111111111_opy_])
      except Exception as e:
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡨࡸࡦ࡯࡬ࡴ࠼ࠣࡿࢂࠨპ").format(str(e)))
      i += 1
      t.start()
    for t in bstack11111l11_opy_:
      t.join()
    return list(bstack1llll1lll_opy_)