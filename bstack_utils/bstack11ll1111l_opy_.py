# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
import json
from bstack_utils.bstack1l1l1llll1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll111lll_opy_(object):
  bstack111l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠧࡿࠩῆ")), bstack11lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨῇ"))
  bstack1lllll11l111_opy_ = os.path.join(bstack111l11l1l_opy_, bstack11lll1_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶ࠲࡯ࡹ࡯࡯ࠩῈ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1l111lll1_opy_ = None
  bstack1l11lll1ll_opy_ = None
  bstack1lllll111ll1_opy_ = None
  bstack1lllll11l1l1_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11lll1_opy_ (u"ࠪ࡭ࡳࡹࡴࡢࡰࡦࡩࠬΈ")):
      cls.instance = super(bstack1lllll111lll_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll11l11l_opy_()
    return cls.instance
  def bstack1lllll11l11l_opy_(self):
    try:
      with open(self.bstack1lllll11l111_opy_, bstack11lll1_opy_ (u"ࠫࡷ࠭Ὴ")) as bstack1ll11l1ll1_opy_:
        bstack1lllll11l1ll_opy_ = bstack1ll11l1ll1_opy_.read()
        data = json.loads(bstack1lllll11l1ll_opy_)
        if bstack11lll1_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧΉ") in data:
          self.bstack1lllll111l11_opy_(data[bstack11lll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨῌ")])
        if bstack11lll1_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ῍") in data:
          self.bstack11ll111111_opy_(data[bstack11lll1_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ῎")])
        if bstack11lll1_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭῏") in data:
          self.bstack1lllll111l1l_opy_(data[bstack11lll1_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧῐ")])
    except:
      pass
  def bstack1lllll111l1l_opy_(self, bstack1lllll11l1l1_opy_):
    if bstack1lllll11l1l1_opy_ != None:
      self.bstack1lllll11l1l1_opy_ = bstack1lllll11l1l1_opy_
  def bstack11ll111111_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11lll1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩῑ"),bstack11lll1_opy_ (u"ࠬ࠭ῒ"))
      self.bstack1l111lll1_opy_ = scripts.get(bstack11lll1_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪΐ"),bstack11lll1_opy_ (u"ࠧࠨ῔"))
      self.bstack1l11lll1ll_opy_ = scripts.get(bstack11lll1_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬ῕"),bstack11lll1_opy_ (u"ࠩࠪῖ"))
      self.bstack1lllll111ll1_opy_ = scripts.get(bstack11lll1_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨῗ"),bstack11lll1_opy_ (u"ࠫࠬῘ"))
  def bstack1lllll111l11_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll11l111_opy_, bstack11lll1_opy_ (u"ࠬࡽࠧῙ")) as file:
        json.dump({
          bstack11lll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࠣῚ"): self.commands_to_wrap,
          bstack11lll1_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࡳࠣΊ"): {
            bstack11lll1_opy_ (u"ࠣࡵࡦࡥࡳࠨ῜"): self.perform_scan,
            bstack11lll1_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨ῝"): self.bstack1l111lll1_opy_,
            bstack11lll1_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢ῞"): self.bstack1l11lll1ll_opy_,
            bstack11lll1_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤ῟"): self.bstack1lllll111ll1_opy_
          },
          bstack11lll1_opy_ (u"ࠧࡴ࡯࡯ࡄࡖࡸࡦࡩ࡫ࡊࡰࡩࡶࡦࡇ࠱࠲ࡻࡆ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠤῠ"): self.bstack1lllll11l1l1_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡩ࡯࡮࡯ࡤࡲࡩࡹ࠺ࠡࡽࢀࠦῡ").format(e))
      pass
  def bstack1l11l11l1_opy_(self, command_name):
    try:
      return any(command.get(bstack11lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬῢ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11ll1111l_opy_ = bstack1lllll111lll_opy_()