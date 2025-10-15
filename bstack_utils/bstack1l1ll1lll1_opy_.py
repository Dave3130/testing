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
import os
import json
from bstack_utils.bstack1ll1ll111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1l1l11_opy_(object):
  bstack1l1l1lllll_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠨࢀࠪᾤ")), bstack1ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩᾥ"))
  bstack1lllll1l1ll1_opy_ = os.path.join(bstack1l1l1lllll_opy_, bstack1ll1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࠳ࡰࡳࡰࡰࠪᾦ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1l1ll111l1_opy_ = None
  bstack1llll1111l_opy_ = None
  bstack1lllll1l1111_opy_ = None
  bstack1lllll11llll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1ll1l_opy_ (u"ࠫ࡮ࡴࡳࡵࡣࡱࡧࡪ࠭ᾧ")):
      cls.instance = super(bstack1lllll1l1l11_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll1l1l1l_opy_()
    return cls.instance
  def bstack1lllll1l1l1l_opy_(self):
    try:
      with open(self.bstack1lllll1l1ll1_opy_, bstack1ll1l_opy_ (u"ࠬࡸࠧᾨ")) as bstack1lll11l11_opy_:
        bstack1lllll1l11ll_opy_ = bstack1lll11l11_opy_.read()
        data = json.loads(bstack1lllll1l11ll_opy_)
        if bstack1ll1l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨᾩ") in data:
          self.bstack1lllll1l111l_opy_(data[bstack1ll1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩᾪ")])
        if bstack1ll1l_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩᾫ") in data:
          self.bstack1l11l111ll_opy_(data[bstack1ll1l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪᾬ")])
        if bstack1ll1l_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᾭ") in data:
          self.bstack1lllll1l11l1_opy_(data[bstack1ll1l_opy_ (u"ࠫࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᾮ")])
    except:
      pass
  def bstack1lllll1l11l1_opy_(self, bstack1lllll11llll_opy_):
    if bstack1lllll11llll_opy_ != None:
      self.bstack1lllll11llll_opy_ = bstack1lllll11llll_opy_
  def bstack1l11l111ll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1ll1l_opy_ (u"ࠬࡹࡣࡢࡰࠪᾯ"),bstack1ll1l_opy_ (u"࠭ࠧᾰ"))
      self.bstack1l1ll111l1_opy_ = scripts.get(bstack1ll1l_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫᾱ"),bstack1ll1l_opy_ (u"ࠨࠩᾲ"))
      self.bstack1llll1111l_opy_ = scripts.get(bstack1ll1l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ᾳ"),bstack1ll1l_opy_ (u"ࠪࠫᾴ"))
      self.bstack1lllll1l1111_opy_ = scripts.get(bstack1ll1l_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩ᾵"),bstack1ll1l_opy_ (u"ࠬ࠭ᾶ"))
  def bstack1lllll1l111l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1l1ll1_opy_, bstack1ll1l_opy_ (u"࠭ࡷࠨᾷ")) as file:
        json.dump({
          bstack1ll1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤᾸ"): self.commands_to_wrap,
          bstack1ll1l_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤᾹ"): {
            bstack1ll1l_opy_ (u"ࠤࡶࡧࡦࡴࠢᾺ"): self.perform_scan,
            bstack1ll1l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢΆ"): self.bstack1l1ll111l1_opy_,
            bstack1ll1l_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣᾼ"): self.bstack1llll1111l_opy_,
            bstack1ll1l_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥ᾽"): self.bstack1lllll1l1111_opy_
          },
          bstack1ll1l_opy_ (u"ࠨ࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠥι"): self.bstack1lllll11llll_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1ll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࠻ࠢࡾࢁࠧ᾿").format(e))
      pass
  def bstack11ll1111ll_opy_(self, command_name):
    try:
      return any(command.get(bstack1ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭῀")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1l1ll1lll1_opy_ = bstack1lllll1l1l11_opy_()