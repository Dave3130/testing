# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
import json
from bstack_utils.bstack11111l1l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll11lll1_opy_(object):
  bstack1l11l1111_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠨࢀࠪ῀")), bstack11l11l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ῁"))
  bstack1lllll11l111_opy_ = os.path.join(bstack1l11l1111_opy_, bstack11l11l1_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࠳ࡰࡳࡰࡰࠪῂ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1l1l1lll1_opy_ = None
  bstack111ll11lll_opy_ = None
  bstack1lllll11l11l_opy_ = None
  bstack1lllll11l1l1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l11l1_opy_ (u"ࠫ࡮ࡴࡳࡵࡣࡱࡧࡪ࠭ῃ")):
      cls.instance = super(bstack1lllll11lll1_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11ll11_opy_()
    return cls.instance
  def bstack1lllll11ll11_opy_(self):
    try:
      with open(self.bstack1lllll11l111_opy_, bstack11l11l1_opy_ (u"ࠬࡸࠧῄ")) as bstack11l111l11l_opy_:
        bstack1lllll11ll1l_opy_ = bstack11l111l11l_opy_.read()
        data = json.loads(bstack1lllll11ll1l_opy_)
        if bstack11l11l1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ῅") in data:
          self.bstack1lllll111lll_opy_(data[bstack11l11l1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩῆ")])
        if bstack11l11l1_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩῇ") in data:
          self.bstack1ll111ll1_opy_(data[bstack11l11l1_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪῈ")])
        if bstack11l11l1_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧΈ") in data:
          self.bstack1lllll11l1ll_opy_(data[bstack11l11l1_opy_ (u"ࠫࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨῊ")])
    except:
      pass
  def bstack1lllll11l1ll_opy_(self, bstack1lllll11l1l1_opy_):
    if bstack1lllll11l1l1_opy_ != None:
      self.bstack1lllll11l1l1_opy_ = bstack1lllll11l1l1_opy_
  def bstack1ll111ll1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11l11l1_opy_ (u"ࠬࡹࡣࡢࡰࠪΉ"),bstack11l11l1_opy_ (u"࠭ࠧῌ"))
      self.bstack1l1l1lll1_opy_ = scripts.get(bstack11l11l1_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫ῍"),bstack11l11l1_opy_ (u"ࠨࠩ῎"))
      self.bstack111ll11lll_opy_ = scripts.get(bstack11l11l1_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭῏"),bstack11l11l1_opy_ (u"ࠪࠫῐ"))
      self.bstack1lllll11l11l_opy_ = scripts.get(bstack11l11l1_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩῑ"),bstack11l11l1_opy_ (u"ࠬ࠭ῒ"))
  def bstack1lllll111lll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll11l111_opy_, bstack11l11l1_opy_ (u"࠭ࡷࠨΐ")) as file:
        json.dump({
          bstack11l11l1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤ῔"): self.commands_to_wrap,
          bstack11l11l1_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤ῕"): {
            bstack11l11l1_opy_ (u"ࠤࡶࡧࡦࡴࠢῖ"): self.perform_scan,
            bstack11l11l1_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢῗ"): self.bstack1l1l1lll1_opy_,
            bstack11l11l1_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣῘ"): self.bstack111ll11lll_opy_,
            bstack11l11l1_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥῙ"): self.bstack1lllll11l11l_opy_
          },
          bstack11l11l1_opy_ (u"ࠨ࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠥῚ"): self.bstack1lllll11l1l1_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11l11l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࠻ࠢࡾࢁࠧΊ").format(e))
      pass
  def bstack11l1llll1_opy_(self, command_name):
    try:
      return any(command.get(bstack11l11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭῜")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1lllll111l_opy_ = bstack1lllll11lll1_opy_()