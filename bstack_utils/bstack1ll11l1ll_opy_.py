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
import os
import json
from bstack_utils.bstack11ll1ll1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll111l11_opy_(object):
  bstack1l111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack1l111ll_opy_ (u"ࠨࢀࠪῇ")), bstack1l111ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩῈ"))
  bstack1lllll111l1l_opy_ = os.path.join(bstack1l111ll1l1_opy_, bstack1l111ll_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࠳ࡰࡳࡰࡰࠪΈ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1lllll111l_opy_ = None
  bstack11ll11lll1_opy_ = None
  bstack1lllll11l11l_opy_ = None
  bstack1lllll111lll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l111ll_opy_ (u"ࠫ࡮ࡴࡳࡵࡣࡱࡧࡪ࠭Ὴ")):
      cls.instance = super(bstack1lllll111l11_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11l1l1_opy_()
    return cls.instance
  def bstack1lllll11l1l1_opy_(self):
    try:
      with open(self.bstack1lllll111l1l_opy_, bstack1l111ll_opy_ (u"ࠬࡸࠧΉ")) as bstack111l1l1l1l_opy_:
        bstack1lllll111ll1_opy_ = bstack111l1l1l1l_opy_.read()
        data = json.loads(bstack1lllll111ll1_opy_)
        if bstack1l111ll_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨῌ") in data:
          self.bstack1lllll1111ll_opy_(data[bstack1l111ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ῍")])
        if bstack1l111ll_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ῎") in data:
          self.bstack11l1l1lll_opy_(data[bstack1l111ll_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ῏")])
        if bstack1l111ll_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧῐ") in data:
          self.bstack1lllll11l111_opy_(data[bstack1l111ll_opy_ (u"ࠫࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨῑ")])
    except:
      pass
  def bstack1lllll11l111_opy_(self, bstack1lllll111lll_opy_):
    if bstack1lllll111lll_opy_ != None:
      self.bstack1lllll111lll_opy_ = bstack1lllll111lll_opy_
  def bstack11l1l1lll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1l111ll_opy_ (u"ࠬࡹࡣࡢࡰࠪῒ"),bstack1l111ll_opy_ (u"࠭ࠧΐ"))
      self.bstack1lllll111l_opy_ = scripts.get(bstack1l111ll_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫ῔"),bstack1l111ll_opy_ (u"ࠨࠩ῕"))
      self.bstack11ll11lll1_opy_ = scripts.get(bstack1l111ll_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ῖ"),bstack1l111ll_opy_ (u"ࠪࠫῗ"))
      self.bstack1lllll11l11l_opy_ = scripts.get(bstack1l111ll_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩῘ"),bstack1l111ll_opy_ (u"ࠬ࠭Ῑ"))
  def bstack1lllll1111ll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll111l1l_opy_, bstack1l111ll_opy_ (u"࠭ࡷࠨῚ")) as file:
        json.dump({
          bstack1l111ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤΊ"): self.commands_to_wrap,
          bstack1l111ll_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤ῜"): {
            bstack1l111ll_opy_ (u"ࠤࡶࡧࡦࡴࠢ῝"): self.perform_scan,
            bstack1l111ll_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢ῞"): self.bstack1lllll111l_opy_,
            bstack1l111ll_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣ῟"): self.bstack11ll11lll1_opy_,
            bstack1l111ll_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥῠ"): self.bstack1lllll11l11l_opy_
          },
          bstack1l111ll_opy_ (u"ࠨ࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠥῡ"): self.bstack1lllll111lll_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1l111ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࠻ࠢࡾࢁࠧῢ").format(e))
      pass
  def bstack1lll111l11_opy_(self, command_name):
    try:
      return any(command.get(bstack1l111ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ΰ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1ll11l1ll_opy_ = bstack1lllll111l11_opy_()