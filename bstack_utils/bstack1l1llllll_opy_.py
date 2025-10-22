# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
import json
from bstack_utils.bstack111l11ll1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1111ll_opy_(object):
  bstack11lll1l111_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠧࡿࠩῆ")), bstack11l1l11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨῇ"))
  bstack1lllll111ll1_opy_ = os.path.join(bstack11lll1l111_opy_, bstack11l1l11_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶ࠲࡯ࡹ࡯࡯ࠩῈ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1111l11111_opy_ = None
  bstack1ll1l11111_opy_ = None
  bstack1lllll11l11l_opy_ = None
  bstack1lllll11l1l1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l1l11_opy_ (u"ࠪ࡭ࡳࡹࡴࡢࡰࡦࡩࠬΈ")):
      cls.instance = super(bstack1lllll1111ll_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11l111_opy_()
    return cls.instance
  def bstack1lllll11l111_opy_(self):
    try:
      with open(self.bstack1lllll111ll1_opy_, bstack11l1l11_opy_ (u"ࠫࡷ࠭Ὴ")) as bstack11l11l11l_opy_:
        bstack1lllll111l11_opy_ = bstack11l11l11l_opy_.read()
        data = json.loads(bstack1lllll111l11_opy_)
        if bstack11l1l11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧΉ") in data:
          self.bstack1lllll111l1l_opy_(data[bstack11l1l11_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨῌ")])
        if bstack11l1l11_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ῍") in data:
          self.bstack11lll1l1l1_opy_(data[bstack11l1l11_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ῎")])
        if bstack11l1l11_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭῏") in data:
          self.bstack1lllll111lll_opy_(data[bstack11l1l11_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧῐ")])
    except:
      pass
  def bstack1lllll111lll_opy_(self, bstack1lllll11l1l1_opy_):
    if bstack1lllll11l1l1_opy_ != None:
      self.bstack1lllll11l1l1_opy_ = bstack1lllll11l1l1_opy_
  def bstack11lll1l1l1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11l1l11_opy_ (u"ࠫࡸࡩࡡ࡯ࠩῑ"),bstack11l1l11_opy_ (u"ࠬ࠭ῒ"))
      self.bstack1111l11111_opy_ = scripts.get(bstack11l1l11_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪΐ"),bstack11l1l11_opy_ (u"ࠧࠨ῔"))
      self.bstack1ll1l11111_opy_ = scripts.get(bstack11l1l11_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬ῕"),bstack11l1l11_opy_ (u"ࠩࠪῖ"))
      self.bstack1lllll11l11l_opy_ = scripts.get(bstack11l1l11_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨῗ"),bstack11l1l11_opy_ (u"ࠫࠬῘ"))
  def bstack1lllll111l1l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll111ll1_opy_, bstack11l1l11_opy_ (u"ࠬࡽࠧῙ")) as file:
        json.dump({
          bstack11l1l11_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࠣῚ"): self.commands_to_wrap,
          bstack11l1l11_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࡳࠣΊ"): {
            bstack11l1l11_opy_ (u"ࠣࡵࡦࡥࡳࠨ῜"): self.perform_scan,
            bstack11l1l11_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨ῝"): self.bstack1111l11111_opy_,
            bstack11l1l11_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢ῞"): self.bstack1ll1l11111_opy_,
            bstack11l1l11_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤ῟"): self.bstack1lllll11l11l_opy_
          },
          bstack11l1l11_opy_ (u"ࠧࡴ࡯࡯ࡄࡖࡸࡦࡩ࡫ࡊࡰࡩࡶࡦࡇ࠱࠲ࡻࡆ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠤῠ"): self.bstack1lllll11l1l1_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11l1l11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡩ࡯࡮࡯ࡤࡲࡩࡹ࠺ࠡࡽࢀࠦῡ").format(e))
      pass
  def bstack11llll1l1_opy_(self, command_name):
    try:
      return any(command.get(bstack11l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬῢ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1l1llllll_opy_ = bstack1lllll1111ll_opy_()