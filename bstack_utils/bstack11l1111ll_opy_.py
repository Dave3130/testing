# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
import json
from bstack_utils.bstack1ll1111l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll11l1ll_opy_(object):
  bstack1l1ll1ll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠩࢁࠫ῁")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪῂ"))
  bstack1lllll11ll11_opy_ = os.path.join(bstack1l1ll1ll1l_opy_, bstack1l1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠴ࡪࡴࡱࡱࠫῃ"))
  commands_to_wrap = None
  perform_scan = None
  bstack111111lll1_opy_ = None
  bstack1lll11111l_opy_ = None
  bstack1lllll11ll1l_opy_ = None
  bstack1lllll11l1l1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l1_opy_ (u"ࠬ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠧῄ")):
      cls.instance = super(bstack1lllll11l1ll_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11l11l_opy_()
    return cls.instance
  def bstack1lllll11l11l_opy_(self):
    try:
      with open(self.bstack1lllll11ll11_opy_, bstack1l1_opy_ (u"࠭ࡲࠨ῅")) as bstack11llll1l1l_opy_:
        bstack1lllll11lll1_opy_ = bstack11llll1l1l_opy_.read()
        data = json.loads(bstack1lllll11lll1_opy_)
        if bstack1l1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩῆ") in data:
          self.bstack1lllll11l111_opy_(data[bstack1l1_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪῇ")])
        if bstack1l1_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪῈ") in data:
          self.bstack1l1l1ll11_opy_(data[bstack1l1_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫΈ")])
        if bstack1l1_opy_ (u"ࠫࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨῊ") in data:
          self.bstack1lllll111lll_opy_(data[bstack1l1_opy_ (u"ࠬࡴ࡯࡯ࡄࡖࡸࡦࡩ࡫ࡊࡰࡩࡶࡦࡇ࠱࠲ࡻࡆ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩΉ")])
    except:
      pass
  def bstack1lllll111lll_opy_(self, bstack1lllll11l1l1_opy_):
    if bstack1lllll11l1l1_opy_ != None:
      self.bstack1lllll11l1l1_opy_ = bstack1lllll11l1l1_opy_
  def bstack1l1l1ll11_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1l1_opy_ (u"࠭ࡳࡤࡣࡱࠫῌ"),bstack1l1_opy_ (u"ࠧࠨ῍"))
      self.bstack111111lll1_opy_ = scripts.get(bstack1l1_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠬ῎"),bstack1l1_opy_ (u"ࠩࠪ῏"))
      self.bstack1lll11111l_opy_ = scripts.get(bstack1l1_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧῐ"),bstack1l1_opy_ (u"ࠫࠬῑ"))
      self.bstack1lllll11ll1l_opy_ = scripts.get(bstack1l1_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪῒ"),bstack1l1_opy_ (u"࠭ࠧΐ"))
  def bstack1lllll11l111_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll11ll11_opy_, bstack1l1_opy_ (u"ࠧࡸࠩ῔")) as file:
        json.dump({
          bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡵࠥ῕"): self.commands_to_wrap,
          bstack1l1_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࡵࠥῖ"): {
            bstack1l1_opy_ (u"ࠥࡷࡨࡧ࡮ࠣῗ"): self.perform_scan,
            bstack1l1_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠣῘ"): self.bstack111111lll1_opy_,
            bstack1l1_opy_ (u"ࠧ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࡕࡸࡱࡲࡧࡲࡺࠤῙ"): self.bstack1lll11111l_opy_,
            bstack1l1_opy_ (u"ࠨࡳࡢࡸࡨࡖࡪࡹࡵ࡭ࡶࡶࠦῚ"): self.bstack1lllll11ll1l_opy_
          },
          bstack1l1_opy_ (u"ࠢ࡯ࡱࡱࡆࡘࡺࡡࡤ࡭ࡌࡲ࡫ࡸࡡࡂ࠳࠴ࡽࡈ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠦΊ"): self.bstack1lllll11l1l1_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡳࡵࡱࡵ࡭ࡳ࡭ࠠࡤࡱࡰࡱࡦࡴࡤࡴ࠼ࠣࡿࢂࠨ῜").format(e))
      pass
  def bstack11l1llll1_opy_(self, command_name):
    try:
      return any(command.get(bstack1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ῝")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11l1111ll_opy_ = bstack1lllll11l1ll_opy_()