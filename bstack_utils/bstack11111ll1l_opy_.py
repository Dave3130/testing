# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
import json
from bstack_utils.bstack11ll1111l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll111lll_opy_(object):
  bstack111lll1ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠨࢀࠪΰ")), bstack1lll11l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩῤ"))
  bstack1lllll111l11_opy_ = os.path.join(bstack111lll1ll1_opy_, bstack1lll11l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࠳ࡰࡳࡰࡰࠪῥ"))
  commands_to_wrap = None
  perform_scan = None
  bstack11l1l1ll1_opy_ = None
  bstack1l111ll1ll_opy_ = None
  bstack1lllll111111_opy_ = None
  bstack1lllll11111l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1lll11l_opy_ (u"ࠫ࡮ࡴࡳࡵࡣࡱࡧࡪ࠭ῦ")):
      cls.instance = super(bstack1lllll111lll_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll111l1l_opy_()
    return cls.instance
  def bstack1lllll111l1l_opy_(self):
    try:
      with open(self.bstack1lllll111l11_opy_, bstack1lll11l_opy_ (u"ࠬࡸࠧῧ")) as bstack111ll11lll_opy_:
        bstack1lllll111ll1_opy_ = bstack111ll11lll_opy_.read()
        data = json.loads(bstack1lllll111ll1_opy_)
        if bstack1lll11l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨῨ") in data:
          self.bstack1lllll1111l1_opy_(data[bstack1lll11l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩῩ")])
        if bstack1lll11l_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩῪ") in data:
          self.bstack1l11llllll_opy_(data[bstack1lll11l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪΎ")])
        if bstack1lll11l_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧῬ") in data:
          self.bstack1lllll1111ll_opy_(data[bstack1lll11l_opy_ (u"ࠫࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ῭")])
    except:
      pass
  def bstack1lllll1111ll_opy_(self, bstack1lllll11111l_opy_):
    if bstack1lllll11111l_opy_ != None:
      self.bstack1lllll11111l_opy_ = bstack1lllll11111l_opy_
  def bstack1l11llllll_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1lll11l_opy_ (u"ࠬࡹࡣࡢࡰࠪ΅"),bstack1lll11l_opy_ (u"࠭ࠧ`"))
      self.bstack11l1l1ll1_opy_ = scripts.get(bstack1lll11l_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠫ῰"),bstack1lll11l_opy_ (u"ࠨࠩ῱"))
      self.bstack1l111ll1ll_opy_ = scripts.get(bstack1lll11l_opy_ (u"ࠩࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾ࠭ῲ"),bstack1lll11l_opy_ (u"ࠪࠫῳ"))
      self.bstack1lllll111111_opy_ = scripts.get(bstack1lll11l_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩῴ"),bstack1lll11l_opy_ (u"ࠬ࠭῵"))
  def bstack1lllll1111l1_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll111l11_opy_, bstack1lll11l_opy_ (u"࠭ࡷࠨῶ")) as file:
        json.dump({
          bstack1lll11l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤῷ"): self.commands_to_wrap,
          bstack1lll11l_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤῸ"): {
            bstack1lll11l_opy_ (u"ࠤࡶࡧࡦࡴࠢΌ"): self.perform_scan,
            bstack1lll11l_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢῺ"): self.bstack11l1l1ll1_opy_,
            bstack1lll11l_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣΏ"): self.bstack1l111ll1ll_opy_,
            bstack1lll11l_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥῼ"): self.bstack1lllll111111_opy_
          },
          bstack1lll11l_opy_ (u"ࠨ࡮ࡰࡰࡅࡗࡹࡧࡣ࡬ࡋࡱࡪࡷࡧࡁ࠲࠳ࡼࡇ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠥ´"): self.bstack1lllll11111l_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1lll11l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࠻ࠢࡾࢁࠧ῾").format(e))
      pass
  def bstack1ll111ll1l_opy_(self, command_name):
    try:
      return any(command.get(bstack1lll11l_opy_ (u"ࠨࡰࡤࡱࡪ࠭῿")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11111ll1l_opy_ = bstack1lllll111lll_opy_()