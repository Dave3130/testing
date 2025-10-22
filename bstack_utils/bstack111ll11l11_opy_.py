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
import os
import json
from bstack_utils.bstack1l11l1lll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll11l111_opy_(object):
  bstack1lll111ll1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠨࢀࠪῇ")), bstack111l1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩῈ"))
  bstack1lllll11l1l1_opy_ = os.path.join(bstack1lll111ll1_opy_, bstack111l1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࠳ࡰࡳࡰࡰࠪΈ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1111lll1l_opy_ = None
  bstack11ll11llll_opy_ = None
  bstack1lllll111l1l_opy_ = None
  bstack1lllll111l11_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack111l1l_opy_ (u"ࠫ࡮ࡴࡳࡵࡣࡱࡧࡪ࠭Ὴ")):
      cls.instance = super(bstack1lllll11l111_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll1111ll_opy_()
    return cls.instance
  def bstack1lllll1111ll_opy_(self):
    try:
      with open(self.bstack1lllll11l1l1_opy_, bstack111l1l_opy_ (u"ࠬࡸࠧΉ")) as bstack1l111111ll_opy_:
        bstack1lllll111lll_opy_ = bstack1l111111ll_opy_.read()
        data = json.loads(bstack1lllll111lll_opy_)
        if bstack111l1l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨῌ") in data:
          self.bstack1lllll11l11l_opy_(data[bstack111l1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ῍")])
        if bstack111l1l_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ῎") in data:
          self.bstack11llll11l_opy_(data[bstack111l1l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ῏")])
        if bstack111l1l_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧῐ") in data:
          self.bstack1lllll111ll1_opy_(data[bstack111l1l_opy_ (u"ࠫࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨῑ")])
    except:
      pass
  def bstack1lllll111ll1_opy_(self, bstack1lllll111l11_opy_):
    if bstack1lllll111l11_opy_ != None:
      self.bstack1lllll111l11_opy_ = bstack1lllll111l11_opy_
  def bstack11llll11l_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack111l1l_opy_ (u"ࠬࡹࡣࡢࡰࠪῒ"),bstack111l1l_opy_ (u"࠭ࠧΐ"))
      self.bstack1111lll1l_opy_ = scripts.get(bstack111l1l_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫ῔"),bstack111l1l_opy_ (u"ࠨࠩ῕"))
      self.bstack11ll11llll_opy_ = scripts.get(bstack111l1l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ῖ"),bstack111l1l_opy_ (u"ࠪࠫῗ"))
      self.bstack1lllll111l1l_opy_ = scripts.get(bstack111l1l_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩῘ"),bstack111l1l_opy_ (u"ࠬ࠭Ῑ"))
  def bstack1lllll11l11l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll11l1l1_opy_, bstack111l1l_opy_ (u"࠭ࡷࠨῚ")) as file:
        json.dump({
          bstack111l1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤΊ"): self.commands_to_wrap,
          bstack111l1l_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤ῜"): {
            bstack111l1l_opy_ (u"ࠤࡶࡧࡦࡴࠢ῝"): self.perform_scan,
            bstack111l1l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢ῞"): self.bstack1111lll1l_opy_,
            bstack111l1l_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣ῟"): self.bstack11ll11llll_opy_,
            bstack111l1l_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥῠ"): self.bstack1lllll111l1l_opy_
          },
          bstack111l1l_opy_ (u"ࠨ࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠥῡ"): self.bstack1lllll111l11_opy_
        }, file)
    except Exception as e:
      logger.error(bstack111l1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࠻ࠢࡾࢁࠧῢ").format(e))
      pass
  def bstack11llll1ll1_opy_(self, command_name):
    try:
      return any(command.get(bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ΰ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack111ll11l11_opy_ = bstack1lllll11l111_opy_()