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
import os
import json
from bstack_utils.bstack11l1l1l1ll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll111l1l_opy_(object):
  bstack1l1ll1ll11_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠨࢀࠪ῎")), bstack11ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ῏"))
  bstack1lllll11l11l_opy_ = os.path.join(bstack1l1ll1ll11_opy_, bstack11ll_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࠳ࡰࡳࡰࡰࠪῐ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1l1l11l111_opy_ = None
  bstack1ll111ll11_opy_ = None
  bstack1lllll11l1ll_opy_ = None
  bstack1lllll11l111_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11ll_opy_ (u"ࠫ࡮ࡴࡳࡵࡣࡱࡧࡪ࠭ῑ")):
      cls.instance = super(bstack1lllll111l1l_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11l1l1_opy_()
    return cls.instance
  def bstack1lllll11l1l1_opy_(self):
    try:
      with open(self.bstack1lllll11l11l_opy_, bstack11ll_opy_ (u"ࠬࡸࠧῒ")) as bstack11l1111ll1_opy_:
        bstack1lllll111l11_opy_ = bstack11l1111ll1_opy_.read()
        data = json.loads(bstack1lllll111l11_opy_)
        if bstack11ll_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨΐ") in data:
          self.bstack1lllll111lll_opy_(data[bstack11ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ῔")])
        if bstack11ll_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ῕") in data:
          self.bstack1l11l11l1_opy_(data[bstack11ll_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪῖ")])
        if bstack11ll_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧῗ") in data:
          self.bstack1lllll111ll1_opy_(data[bstack11ll_opy_ (u"ࠫࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨῘ")])
    except:
      pass
  def bstack1lllll111ll1_opy_(self, bstack1lllll11l111_opy_):
    if bstack1lllll11l111_opy_ != None:
      self.bstack1lllll11l111_opy_ = bstack1lllll11l111_opy_
  def bstack1l11l11l1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11ll_opy_ (u"ࠬࡹࡣࡢࡰࠪῙ"),bstack11ll_opy_ (u"࠭ࠧῚ"))
      self.bstack1l1l11l111_opy_ = scripts.get(bstack11ll_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫΊ"),bstack11ll_opy_ (u"ࠨࠩ῜"))
      self.bstack1ll111ll11_opy_ = scripts.get(bstack11ll_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭῝"),bstack11ll_opy_ (u"ࠪࠫ῞"))
      self.bstack1lllll11l1ll_opy_ = scripts.get(bstack11ll_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩ῟"),bstack11ll_opy_ (u"ࠬ࠭ῠ"))
  def bstack1lllll111lll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll11l11l_opy_, bstack11ll_opy_ (u"࠭ࡷࠨῡ")) as file:
        json.dump({
          bstack11ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤῢ"): self.commands_to_wrap,
          bstack11ll_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤΰ"): {
            bstack11ll_opy_ (u"ࠤࡶࡧࡦࡴࠢῤ"): self.perform_scan,
            bstack11ll_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢῥ"): self.bstack1l1l11l111_opy_,
            bstack11ll_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣῦ"): self.bstack1ll111ll11_opy_,
            bstack11ll_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥῧ"): self.bstack1lllll11l1ll_opy_
          },
          bstack11ll_opy_ (u"ࠨ࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠥῨ"): self.bstack1lllll11l111_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࠻ࠢࡾࢁࠧῩ").format(e))
      pass
  def bstack11111l1ll_opy_(self, command_name):
    try:
      return any(command.get(bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ὺ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1l1l1l1l1_opy_ = bstack1lllll111l1l_opy_()